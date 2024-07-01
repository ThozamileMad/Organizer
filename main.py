import os
from pathlib import Path


def modify_duplicate(file, des_lst, dir_name):
    file_segs = file.split(".")
    print(file_segs)
    print(file.split(".")[-2][-2])
    try:
        # Finds the last duplicate's number in destination
        dup_num = [filename.split(".")[-2][-2] for filename in des_lst][-1]
        print(dup_num)
        file_segs.insert(-1, f"({dup_num + 1})")
        
        # Creates new file duplicate with new number
        new_dup = "".join(file_segs)

        # Makes duplicate in destination folder
        src = os.path.join(src_path, file) # source path
        des = os.path.join(ext_des[dir_name]["des"], new_dup) # destination path
        os.rename(src, des)
        print(f"{src}  ->  {ext_des[dir_name]['des']} (File Duplicate)")
    except IndexError or ValueError:
        # Defaults to creating first duplicate if not other duplicates exist
        file_segs.insert(-1, f"(1).")
        new_dup = "".join(file_segs)
        
        src = os.path.join(src_path, file) # source path
        des = os.path.join(ext_des[dir_name]["des"], new_dup) # destination path
        os.rename(src, des)
        print(f"{src}  ->  {ext_des[dir_name]['des']} (File Duplicate)")
    

def move_file(file):
    dir_names = ["Pictures", "Documents", "Videos", "Music"]

    for dir_name in dir_names:
        ext = "." + file.split(".")[-1] # File extension
        src = os.path.join(src_path, file) # source path
        des = os.path.join(ext_des[dir_name]["des"], file) # destination path
        in_des = os.path.exists(des) # Checks if file is in destination dir

        src_files = os.listdir(src_path)
        des_files = os.listdir(ext_des[dir_name]["des"])
        if file in src_files and file in des_files:
            modify_duplicate(file, des_files, dir_name) 
        if ext in ext_des[dir_name]["ext"] and not in_des:
            os.rename(src, des) # Moves file to appropriate folder
            global files_moved
            files_moved += 1
            print(f"{src}  ->  {ext_des[dir_name]['des']}")

            

def move_all_files():
    target_dir = os.listdir(src_path) # Files in User Input Directory
    for file in target_dir:
        move_file(file)
    print(f"{files_moved} Files Reorganized.")
    

user_dir = os.path.join(os.path.expanduser("~")) # User's Directory
                        
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

os.chdir("/")
src_path = input("Please Enter The Path of The Target Directory: ")
files_moved = 0
move_all_files()

