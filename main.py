import os
from pathlib import Path

user_dir = os.path.join(os.path.expanduser("~"))
                        
ext_des = {
    "Pictures": {
        "ext": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
        "des": os.path.join(user_dir, "Pictures") 
        },
    "Videos": {
        "ext": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm", ".mpeg"],
        "des": os.path.join(user_dir, "Videos")
        },
    "Documents": {
        "ext": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".md"],
        "des": os.path.join(user_dir, "Documents")
        },
    
    "Music": {
        "ext": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".alac"],
        "des": os.path.join(user_dir, "Music")
        }
}


def is_duplicate_file_path(path):
    if os.path.exists(path):
        return True
    else:
        return False


def get_src_and_des_path(extension_lst, des_path):
    target_dir = os.listdir(src_path)
    paths = []

    for file_path in target_dir:
        for extension in extension_lst:
            # Compares files to extension
            if extension in file_path:
                modified_src_path = os.path.join(src_path, file_path)
                modified_des_path = os.path.join(des_path, file_path)
            
                path_item = {"src_path": modified_src_path,
                             "des_path": modified_des_path,
                             "des_dir": des_path}

                if is_duplicate_file_path(modified_des_path):
                    pass
                elif path_item not in paths:
                    paths.append(path_item)
                    
    return paths


def move_files_based_on_type(src_des_dict):
    for paths in src_des_dict:
        s_path = paths["src_path"]
        d_path = paths["des_path"]
        dir_path = paths['des_dir']
        os.rename(Path(s_path), Path(d_path))
        print(f"File: '{s_path}', moved to: '{dir_path}'")


def move_all_files():
    try:
        path_data = [get_src_and_des_path(ext_des[key]["ext"], ext_des[key]["des"])
                     for key in ext_des
                     if len(get_src_and_des_path(ext_des[key]["ext"], ext_des[key]["des"])) != 0]
        
        for lst in path_data:
            move_files_based_on_type(lst)
            
        if len(path_data) != 0: 
            print("All FILES REARRANGED")
        
    except FileNotFoundError:
        print("Sorry File Not Found!!! Please Enter a valid file path.")


os.chdir("/")
src_path = input("Please Enter The Path of The Target Directory: ")
# Moves every file to it's appropriate folders (.mp3 to Music, .jpg to Pictures)
move_all_files()

# C:\Users\Church\Downloads
