from pathlib import Path

# folder where we will create files
folder = Path("files")

folder.mkdir(exist_ok=True)

for i in range(1, 21):  # creates 20 files
    file_path = folder / f"document{i}.txt"
    file_path.write_text(f"This is file number {i}")
