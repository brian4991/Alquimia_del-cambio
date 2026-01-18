import React, { useState, useEffect } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

// Styles personnalisés pour un éditeur compact
const miniEditorStyles = `
  .mini-rich-editor .ql-editor {
    min-height: 80px;
    padding: 12px;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    line-height: 1.5;
  }
  .mini-rich-editor .ql-container {
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    border: 1px solid #e5e7eb;
    border-top: none;
  }
  .mini-rich-editor .ql-toolbar {
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    border: 1px solid #e5e7eb;
    background: #f9fafb;
    padding: 6px 8px;
  }
  .mini-rich-editor .ql-toolbar .ql-formats {
    margin-right: 8px;
  }
  .mini-rich-editor .ql-toolbar button {
    padding: 4px 6px;
    border-radius: 4px;
    width: 26px;
    height: 26px;
  }
  .mini-rich-editor .ql-toolbar button:hover {
    background: #e5e7eb;
  }
  .mini-rich-editor .ql-toolbar button.ql-active {
    background: #6b745a;
    color: white;
  }
  .mini-rich-editor .ql-toolbar button.ql-active .ql-stroke {
    stroke: white;
  }
  .mini-rich-editor .ql-toolbar button.ql-active .ql-fill {
    fill: white;
  }
  .mini-rich-editor .ql-color .ql-picker-options {
    padding: 6px;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  .mini-rich-editor .ql-color .ql-picker-item {
    border-radius: 2px;
    margin: 1px;
    width: 18px;
    height: 18px;
  }
  .mini-rich-editor .ql-picker-label {
    padding: 2px 4px;
  }
  .mini-rich-editor .ql-snow .ql-picker.ql-header {
    width: 90px;
  }
  
  /* Style pour le mode compact (questions) */
  .mini-rich-editor.compact .ql-editor {
    min-height: 60px;
  }
  .mini-rich-editor.compact .ql-toolbar {
    padding: 4px 6px;
  }
`;

const MiniRichTextEditor = ({ 
  value, 
  onChange, 
  placeholder = "Écrivez ici...",
  minHeight = 80,
  compact = false,
  className = ""
}) => {
  const [content, setContent] = useState(value || '');

  useEffect(() => {
    setContent(value || '');
  }, [value]);

  const handleChange = (newContent) => {
    setContent(newContent);
    if (onChange) {
      // Clean empty content
      const cleanedContent = newContent === '<p><br></p>' ? '' : newContent;
      onChange(cleanedContent);
    }
  };

  // Configuration de la barre d'outils - version compacte
  const modules = {
    toolbar: compact ? [
      ['bold', 'italic', 'underline'],
      [{ 'color': [
        '#000000', '#e60000', '#ff9900', '#008a00', '#0066cc', '#9933ff',
        '#6b745a', '#8a9373', '#ea580c', '#dc2626'
      ] }],
      ['clean']
    ] : [
      [{ 'header': [1, 2, 3, false] }],
      ['bold', 'italic', 'underline', 'strike'],
      [{ 'color': [
        '#000000', '#e60000', '#ff9900', '#ffff00', '#008a00', '#0066cc', '#9933ff',
        '#ffffff', '#facccc', '#ffebcc', '#ffffcc', '#cce8cc', '#cce0f5', '#ebd6ff',
        '#6b745a', '#8a9373', '#5a6349', '#ea580c', '#dc2626', '#f97316'
      ] }, { 'background': [
        '#ffffff', '#facccc', '#ffebcc', '#ffffcc', '#cce8cc', '#cce0f5', '#ebd6ff',
        '#f3f4f6', '#fef3c7', '#dcfce7', '#dbeafe', '#fce7f3'
      ] }],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'align': [] }],
      ['clean']
    ],
  };

  const formats = compact 
    ? ['bold', 'italic', 'underline', 'color']
    : ['header', 'bold', 'italic', 'underline', 'strike', 'color', 'background', 'list', 'bullet', 'align'];

  return (
    <div className={`mini-rich-editor ${compact ? 'compact' : ''} ${className}`}>
      <style>{miniEditorStyles}</style>
      <ReactQuill
        theme="snow"
        value={content}
        onChange={handleChange}
        modules={modules}
        formats={formats}
        placeholder={placeholder}
        style={{ 
          backgroundColor: 'white',
          borderRadius: '8px'
        }}
      />
    </div>
  );
};

export default MiniRichTextEditor;
