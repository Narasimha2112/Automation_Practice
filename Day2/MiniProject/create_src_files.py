from pathlib import Path
import shutil

src = Path("src_files")
src.mkdir(exist_ok=True)

extensions = [".jpg", ".png", ".pdf", ".txt", ".docx", ".mp3", ".wav", ".mp4", ".mkv", ".zip", ".rar", ".java", ".py"]

for i, ext in enumerate(extensions, start=1):
    file_path = src / f"file{i}{ext}"
    file_path.write_text(f"This is a test file with extension {ext}")

        