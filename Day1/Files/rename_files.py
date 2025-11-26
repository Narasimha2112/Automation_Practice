from pathlib import Path

# folder where files are located
folder = Path("files")

# list all .txt files inside the folder
txt_files = sorted(folder.glob("*.txt"))

for index, report in enumerate(txt_files, start=1):
    if not report.name.startswith("file_0"):
        continue  # skip this file
    
    # create new name with 3 digits, e.g. 001, 002, 010, 020
    new_name = f"report_{index:03}.txt"
    new_path = report.with_name(new_name)
    
    print(f"Renaming {report.name} to {new_name}")
    report.rename(new_path)
    
print("Renaming completed.")
    
    