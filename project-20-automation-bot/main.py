
## main.py

```python
import os
import shutil

source_folder = "files"
destination_folder = "organized"

file_types = {
    "images": [".jpg", ".png", ".jpeg"],
    "documents": [".pdf", ".docx", ".txt"],
    "scripts": [".py", ".sh"],
    "others": []
}


def create_folders():
    os.makedirs(destination_folder, exist_ok=True)

    for folder_name in file_types.keys():
        os.makedirs(os.path.join(destination_folder, folder_name), exist_ok=True)


def get_destination_subfolder(file_name):
    _, extension = os.path.splitext(file_name.lower())

    for folder_name, extensions in file_types.items():
        if extension in extensions:
            return folder_name

    return "others"


def organize_files():
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    create_folders()

    moved_files = 0

    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)

        if os.path.isfile(source_path):
            subfolder = get_destination_subfolder(file_name)
            destination_path = os.path.join(destination_folder, subfolder, file_name)

            shutil.move(source_path, destination_path)
            moved_files += 1
            print(f"Moved: {file_name} -> {subfolder}")

    print(f"\nAutomation completed successfully. {moved_files} file(s) moved.")


if __name__ == "__main__":
    organize_files()
