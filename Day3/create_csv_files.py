from pathlib import Path
import csv

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

#Sample sales data for 3 regions
files_data = {
    "sales_north.csv": [
        ["id", "product", "region", "quantity", "price"],
        [1, "Laptop", "North", 3, 50000],
        [2, "Mouse", "North", 10, 500],
        [3, "KeyBoard", "North", 5, 800],
    ],
    "sales_south.csv": [
        ["id", "product", "region", "quantity", "price"],
        [4, "Laptop", "South", 4, 80000],
        [5, "Mouse", "South", 15, 1200],
        [6, "KeyBoard", "South", 4, 1800],
    ],
    "sales_east.csv": [
        ["id", "product", "region", "quantity", "price"],
        [7, "Laptop", "east", 1, 51000],
        [8, "Mouse", "east", 7, 750],
        [9, "KeyBoard", "east", 3, 1400],
    ],
}

for filename, rows in files_data.items():
    file_path = data_folder / filename
    with file_path.open(mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
        
    print(f"Created {filename}")