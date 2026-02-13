"""
StyleSense Database Management Utility
Run this to initialize or reset the database
"""

import os
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / 'backend'
sys.path.insert(0, str(backend_path))

from app import app, db

def init_db():
    """Initialize the database"""
    print("🗄️  Initializing StyleSense Database...")
    with app.app_context():
        db.create_all()
    print("✅ Database initialized successfully!")

def reset_db():
    """Reset the database (WARNING: Deletes all data)"""
    print("⚠️  WARNING: This will delete all data!")
    confirm = input("Type 'yes' to confirm database reset: ")
    
    if confirm.lower() == 'yes':
        with app.app_context():
            db.drop_all()
            db.create_all()
        print("✅ Database reset successfully!")
    else:
        print("❌ Database reset cancelled")

def show_stats():
    """Show database statistics"""
    with app.app_context():
        from app import UserPreference, SavedOutfit, OutfitAnalysis
        
        users = UserPreference.query.count()
        outfits = SavedOutfit.query.count()
        analyses = OutfitAnalysis.query.count()
        
        print("\n📊 StyleSense Database Statistics:")
        print(f"   👥 User Preferences: {users}")
        print(f"   👗 Saved Outfits: {outfits}")
        print(f"   📷 Image Analyses: {analyses}")
        print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("StyleSense Database Manager")
        print("===========================")
        print("\nUsage:")
        print("  python manage_db.py init   - Initialize database")
        print("  python manage_db.py reset  - Reset database (deletes all data)")
        print("  python manage_db.py stats  - Show database statistics")
    else:
        command = sys.argv[1].lower()
        
        if command == 'init':
            init_db()
        elif command == 'reset':
            reset_db()
        elif command == 'stats':
            show_stats()
        else:
            print(f"❌ Unknown command: {command}")
