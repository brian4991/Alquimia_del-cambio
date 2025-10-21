"""
Migration script to create page_contents table
"""
from database import engine, SessionLocal
from models import Base, PageContent

def migrate():
    print("Creating page_contents table...")
    
    # Create all tables (will only create missing ones)
    Base.metadata.create_all(bind=engine)
    
    print("✓ page_contents table created successfully")
    
    # Initialize default content for landing pages
    db = SessionLocal()
    try:
        # Check if pages already exist
        existing_pages = db.query(PageContent).count()
        if existing_pages == 0:
            print("Initializing default page contents...")
            
            # Initialize empty sections for each landing page
            pages = ['program', 'retiro', 'psychology']
            for page_name in pages:
                page = PageContent(
                    page_name=page_name,
                    sections={}
                )
                db.add(page)
            
            db.commit()
            print(f"✓ Initialized {len(pages)} landing pages with empty content")
        else:
            print(f"✓ Found {existing_pages} existing pages, skipping initialization")
    
    except Exception as e:
        print(f"Error initializing page contents: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    migrate()

