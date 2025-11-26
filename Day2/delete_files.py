from pathlib import Path

folder = Path("sorted_files")

for file in folder.glob("*"):
    print(f"Deleting {file.name}...")
    file.unlink()
    
print("........Successfully Deleted.......")