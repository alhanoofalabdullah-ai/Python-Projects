
## main.py

```python
import os
import shutil

source_folder = "source_files"
backup_folder = "backup_files"


def backup_files():
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    os.makedirs(backup_folder, exist_ok=True)

    files_copied = 0

    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        backup_path = os.path.join(backup_folder, file_name)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, backup_path)
            files_copied += 1
            print(f"Copied: {file_name}")

    print(f"\nBackup completed successfully. {files_copied} file(s) copied.")


if __name__ == "__main__":
    backup_files()
