from pathlib import Path
import shutil

src = Path("src_files")
dest = Path("dest_files")

dest.mkdir(exist_ok=True)

file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

for file in src.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        
        moved = False
        
        for folder_name, ext_list in file_types.items():
            if ext in ext_list:
                target_folder = dest / folder_name
                target_folder.mkdir(exist_ok=True)
                
                print(f"Moving {file.name} -> {folder_name}/")
                shutil.move(str(file), target_folder)
                moved = True
                break
            
        if not moved:
            other = dest / "Others"
            other.mkdir(exist_ok=True)
            print(f"Moving {file.name} -> Others/")
            shutil.move(str(file),other)
            
print("✅ Sorting Completed!!!")