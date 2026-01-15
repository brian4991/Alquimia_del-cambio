"""
Content Indexer Service.

Indexes transcripts and program content into the vector store.
Used to build the knowledge base for RAG.
"""

import os
from typing import List, Dict, Any, Optional
from pathlib import Path

from marketing.services.memory.vector_store import (
    VectorStoreService,
    get_vector_store,
    Document,
)


class ContentIndexer:
    """
    Service for indexing content into the vector store.
    
    Indexes:
    - Instagram transcripts (for voice/style learning)
    - Program content (for topic knowledge)
    - Approved content (for preference learning)
    """
    
    def __init__(
        self,
        vector_store: Optional[VectorStoreService] = None,
        assets_path: Optional[str] = None,
    ) -> None:
        """
        Initialize content indexer.
        
        Args:
            vector_store: Vector store service.
            assets_path: Path to assets directory.
        """
        self._vector_store = vector_store or get_vector_store()
        self._assets_path = Path(assets_path) if assets_path else self._find_assets_path()
    
    def _find_assets_path(self) -> Path:
        """Find the assets directory relative to project root."""
        # Try common locations
        possible_paths = [
            Path("assets"),
            Path("../assets"),
            Path(__file__).parent.parent.parent.parent / "assets",
        ]
        
        for path in possible_paths:
            if path.exists():
                return path.resolve()
        
        raise FileNotFoundError("Could not find assets directory")
    
    async def index_transcripts(self) -> Dict[str, Any]:
        """
        Index all Instagram transcripts.
        
        Returns:
            Stats about indexed documents.
        """
        transcripts_path = self._assets_path / "transcripts"
        
        if not transcripts_path.exists():
            return {"error": "Transcripts directory not found", "indexed": 0}
        
        indexed = 0
        errors = []
        
        for file_path in transcripts_path.glob("*.txt"):
            try:
                content = file_path.read_text(encoding="utf-8").strip()
                
                # Skip empty or very short files
                if len(content) < 50:
                    continue
                
                await self._vector_store.add_document(
                    content=content,
                    metadata={
                        "type": "transcript",
                        "source": "instagram",
                        "filename": file_path.name,
                        "post_id": file_path.stem,
                    }
                )
                indexed += 1
                
            except Exception as e:
                errors.append({"file": file_path.name, "error": str(e)})
        
        return {
            "indexed": indexed,
            "errors": errors,
            "source": str(transcripts_path),
        }
    
    async def index_program_content(self) -> Dict[str, Any]:
        """
        Index program content (guides, exercises, resources).
        
        Returns:
            Stats about indexed documents.
        """
        indexed = 0
        errors = []
        
        # Index main guides
        guide_files = [
            ("1. Guía.txt", "module_1"),
            ("module2_guia.txt", "module_2"),
            ("module_3_guia.txt", "module_3"),
            ("module_4_guia.txt", "module_4"),
            ("module_5_guia.txt", "module_5"),
        ]
        
        for filename, module_id in guide_files:
            file_path = self._assets_path / filename
            if file_path.exists():
                try:
                    content = file_path.read_text(encoding="utf-8")
                    
                    # Split into chunks for better retrieval
                    chunks = self._split_guide_content(content)
                    
                    for i, chunk in enumerate(chunks):
                        await self._vector_store.add_document(
                            content=chunk,
                            metadata={
                                "type": "program_guide",
                                "module": module_id,
                                "filename": filename,
                                "chunk_index": i,
                            }
                        )
                        indexed += 1
                        
                except Exception as e:
                    errors.append({"file": filename, "error": str(e)})
        
        # Index exercises
        exercise_dirs = [
            ("", ["Ejercicio #1 _Historia_.txt", "Ejercicio #2_ _Emociones_.txt", "Ejercicio #3_ _Gestión Emocional_.txt"]),
            ("exercices_module_2", None),
            ("exercices_module_3", None),
            ("exercice_module_4", None),
            ("exercice_module_5", None),
        ]
        
        for dir_name, specific_files in exercise_dirs:
            dir_path = self._assets_path / dir_name if dir_name else self._assets_path
            
            if dir_path.exists():
                files_to_index = specific_files if specific_files else list(dir_path.glob("*.txt"))
                
                for file_item in files_to_index:
                    file_path = dir_path / file_item if isinstance(file_item, str) else file_item
                    
                    if file_path.exists():
                        try:
                            content = file_path.read_text(encoding="utf-8")
                            
                            await self._vector_store.add_document(
                                content=content,
                                metadata={
                                    "type": "exercise",
                                    "directory": dir_name or "root",
                                    "filename": file_path.name,
                                }
                            )
                            indexed += 1
                            
                        except Exception as e:
                            errors.append({"file": str(file_path), "error": str(e)})
        
        # Index resources
        resource_dirs = ["recurso_module1", "recursos_modulke2", "recurso_module3", "recurso_module5"]
        
        for dir_name in resource_dirs:
            dir_path = self._assets_path / dir_name
            
            if dir_path.exists():
                for file_path in dir_path.glob("*.txt"):
                    try:
                        content = file_path.read_text(encoding="utf-8")
                        
                        await self._vector_store.add_document(
                            content=content,
                            metadata={
                                "type": "resource",
                                "directory": dir_name,
                                "filename": file_path.name,
                            }
                        )
                        indexed += 1
                        
                    except Exception as e:
                        errors.append({"file": str(file_path), "error": str(e)})
        
        return {
            "indexed": indexed,
            "errors": errors,
        }
    
    def _split_guide_content(self, content: str, max_chunk_size: int = 2000) -> List[str]:
        """
        Split guide content by sections.
        
        Args:
            content: Full guide content.
            max_chunk_size: Maximum characters per chunk.
            
        Returns:
            List of content chunks.
        """
        # Split by main sections (Tema, Subtema, etc.)
        sections = []
        current_section = []
        current_size = 0
        
        lines = content.split('\n')
        
        for line in lines:
            # Check if this is a section header
            is_header = (
                line.strip().startswith("Tema ") or
                line.strip().startswith("Subtema ") or
                line.strip().startswith("Módulo ") or
                line.strip().startswith("Ejercicio")
            )
            
            if is_header and current_section and current_size > 500:
                # Save current section
                sections.append('\n'.join(current_section))
                current_section = []
                current_size = 0
            
            current_section.append(line)
            current_size += len(line)
            
            # Force split if too large
            if current_size > max_chunk_size:
                sections.append('\n'.join(current_section))
                current_section = []
                current_size = 0
        
        # Add remaining content
        if current_section:
            sections.append('\n'.join(current_section))
        
        return [s.strip() for s in sections if s.strip()]
    
    async def index_all(self) -> Dict[str, Any]:
        """
        Index all content (transcripts + program).
        
        Returns:
            Combined stats from all indexing operations.
        """
        # Initialize vector store
        await self._vector_store.initialize()
        
        # Index all content
        transcript_stats = await self.index_transcripts()
        program_stats = await self.index_program_content()
        
        # Get final stats
        final_stats = await self._vector_store.get_stats()
        
        return {
            "transcripts": transcript_stats,
            "program": program_stats,
            "total": final_stats,
        }
    
    async def reindex_all(self) -> Dict[str, Any]:
        """
        Clear and reindex all content.
        
        Returns:
            Stats from reindexing operation.
        """
        # Clear existing content
        deleted = await self._vector_store.clear_collection()
        
        # Reindex
        stats = await self.index_all()
        stats["deleted_before_reindex"] = deleted
        
        return stats


# Factory function
def get_content_indexer(assets_path: Optional[str] = None) -> ContentIndexer:
    """Create content indexer instance."""
    return ContentIndexer(assets_path=assets_path)
