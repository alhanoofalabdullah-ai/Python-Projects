import os
import shutil

source_folder = "test_folder"

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}


def organize_files():
    if not os.path.exists(source_folder):
        print(f"Folder '{source_folder}' does not exist.")
        return

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    target_folder = os.path.join(source_folder, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved {file} -> {folder}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(source_folder, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved {file} -> Others")


organize_files()
