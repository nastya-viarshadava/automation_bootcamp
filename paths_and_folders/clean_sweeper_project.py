from pathlib import Path
import shutil

while True:
    root_dir = Path(input("Please enter the target folder: "))

    if root_dir.exists():
        break

    print("That's an invalid directory. Please, enter the full path of a valid folder on your machine.")

closet_dir = root_dir / "closet"
closet_dir.mkdir(exist_ok=True)

text_dir = closet_dir / "text_files"
text_dir.mkdir(exist_ok=True)

csv_dir = closet_dir / "csv_files"
csv_dir.mkdir(exist_ok=True)

folders_dir = closet_dir / "folders"
folders_dir.mkdir(exist_ok=True)

for item in root_dir.iterdir():
    if item == closet_dir:
        continue
    elif item.is_file() and item.suffix == ".txt":
        shutil.move(item, text_dir / item.name)
    elif item.is_file() and item.suffix == ".csv":
        shutil.move(item, csv_dir / item.name)
    elif item.is_dir() and "temp" in item.name:
        shutil.rmtree(item)
    elif item.is_dir():
        shutil.move(item, folders_dir / item.name)
    else:
        shutil.move(item, closet_dir / item.name)

print('Folder cleanup complete!')






    if item.is_file() and item.suffix == ".csv":
        src = Path.home() / "documents" / "python_automation" / "project_complete" / "clean_sweep_example_folder"
        dest = Path.home() / 'documents' / 'python_automation' / "project_complete" / 'closet' / 'csv_files'
        if src.exists():
            shutil.move(src, dest)

    if item.is_dir() and "temp" in item.name.lower():
        shutil.rmtree(path)
    else:
        src = Path.home() / "documents" / "python_automation" / "project_complete" / "clean_sweep_example_folder"
        dest = Path.home() / 'documents' / 'python_automation' / "project_complete" / 'closet' / 'folders'
        if src.exists():
            shutil.move(src, dest)



