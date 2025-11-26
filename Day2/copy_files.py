from pathlib import Path
import shutil

source_folder = Path("source_files")
destination_folder = Path("copied_files")

destination_folder.mkdir(exist_ok=True)

for file in source_folder.iterdir():
    if file.is_file():
        print(f"Copying {file.name} to {destination_folder}")
        shutil.copy(file, destination_folder / file.name)
        
print("All files have been copied.")