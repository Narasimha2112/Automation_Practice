from pathlib import Path
import shutil

source_fdr = Path("source_files")
destination_fdr = Path("sorted_files")

destination_fdr.mkdir(exist_ok=True)

for file in source_fdr.iterdir():
    if file.is_file():
        print(f"Moving {file.name} to {destination_fdr}")
        shutil.move(str(file),str(destination_fdr))
        
print("All file have been moved to Sorted Files Folder.....")