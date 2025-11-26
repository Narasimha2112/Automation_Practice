from pathlib import Path
import shutil

folder = Path("source_files")
folder.mkdir(exist_ok=True)

extensions = [".txt", ".pdf", ".jpg", ".mp3", ".mp4", ".png"]

for i, ext in enumerate(extensions, start=1):
    file_path = folder / f"file{i}{ext}"
    file_path.write_text(f"This is a test file with extension {ext}")

