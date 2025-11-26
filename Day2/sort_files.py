from pathlib import Path
import shutil

src = Path("source_files")
dest = Path("sorted_files")

dest.mkdir(exist_ok=True)

file_types = {
    "Images"    : [".jpg", ".png"],
    "Documents" : [".pdf", ".txt"],
    "Music"     : [".mp3"],
    "Videos"    : [".mp4"]
}

for file in src.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                target_folder = dest / folder_name
                target_folder.mkdir(exist_ok=True)
                
                print(f"Moving {file.name} -> {folder_name}/")
                shutil.move(str(file),str(target_folder))
                break