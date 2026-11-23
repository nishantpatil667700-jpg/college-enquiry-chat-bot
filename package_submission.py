"""
Script to package the College Enquiry Chatbot project for submission.
Excludes .env, virtual environments, cache files, and git metadata.
Creates Code.zip ready for Drive upload.
"""
import os
import zipfile
from pathlib import Path

def package_project():
    root_dir = Path(__file__).parent.resolve()
    zip_path = root_dir / "Code.zip"
    
    exclude_dirs = {".venv", "venv", "__pycache__", ".git", ".pytest_cache"}
    exclude_files = {".env", "Code.zip", ".DS_Store"}
    
    print(f"Creating submission zip: {zip_path.name}...")
    file_count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in root_dir.rglob("*"):
            # Skip excluded directories
            if any(part in exclude_dirs for part in file.parts):
                continue
            # Skip excluded files
            if file.name in exclude_files or file.suffix == ".pyc":
                continue
            if file.is_file():
                rel_path = file.relative_to(root_dir)
                zipf.write(file, arcname=rel_path)
                file_count += 1
                print(f"  + Added: {rel_path}")
                
    print(f"\n✅ Successfully created {zip_path.name} ({zip_path.stat().st_size / 1024:.1f} KB) with {file_count} files.")
    print("🔒 Confirmed: .env and virtual environments are strictly excluded!")

if __name__ == "__main__":
    package_project()
