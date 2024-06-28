import os
from pathlib import Path
from pprint import pprint

file_extensions = {
    "Pictures": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"
    ],
    "Videos": [
        ".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm", ".mpeg"
    ],
    "Documents": [
        ".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv", ".md"
    ],
    "Music": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".alac"
    ]
}

target_path = input("Please Enter The Path of The Target Directory: ")
modified_target_path = Path(target_path)

# List of Items In Directory
target_dir = os.listdir(modified_target_path)

# Getting Documents, Videos, Pictures, Music in Users Directory
user_path = f"C:/Users/"
user_items = os.listdir(Path(user_path))


def get_des_paths():
    # Identifies the user's username then obtains destination paths
    for dir in user_items:
        dir_with_onedrive = Path(f"{user_path}{dir}/OneDrive")
        if os.path.isdir(dir_with_onedrive):
            user_name = f"{user_path}{dir}/"
            destination_names = ["Documents", "Videos", "Pictures", "Music"]
            destination_paths = [user_name + des_name for des_name in destination_names]

            return destination_paths


def move_files_to_des(destination_paths):
    # Loops through files in targeted directory
    for filename in target_dir:
        for k, v in file_extensions.items():

            # Identifies source and destination paths
            for ext in v:
                if ext in filename:
                    for des_path in destination_paths:
                        src_path = Path(target_path + "/" + filename)
                        if k in des_path:
                            des_path = Path(des_path + "/" + filename)

                            # Moves file to appropriate Destination (e.g .mp3 to Music Directory)
                            os.rename(src_path, des_path)


destination_paths = get_des_paths()
move_files_to_des(destination_paths)
print("Your Files have been successfully arranged")
