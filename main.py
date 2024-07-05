import os


def modify_duplicate(file, des_lst):
    segs = file.split(".")
    seg = segs[0]

    nums = [f"{num + 1}" for num in range(100)]

    if len(seg) >= 3:
        if f"{seg[-2]}" in nums:
            seg = seg[:-3]

    if len(seg) >= 4:
        if f"{seg[-3]}{seg[-2]}" in nums:
            seg = seg[:-4]

    if len(seg) >= 5:
        if f"{seg[-4]}{seg[-3]}{seg[-2]}" in nums:
            seg = seg[:-5]

    lst = [file for file in des_lst if segs[1] in file]
    new_lst = [item.replace("(", "*").replace(")", "*") for item in lst if seg in item]

    dup_nums = []
    for file in new_lst:
        try:
            mod_file = file.split("*")
            dup_nums.append(int(mod_file[-2]))
        except IndexError:
            pass

    file_num = 1

    for num in range(len(dup_nums)):
        min_num = min(dup_nums)
        if min_num + 1 not in dup_nums:
            file_num = min_num + 1
        else:
            dup_nums.remove(min_num)

    new_file = seg + f"({file_num})" + "." + segs[-1]
    return new_file


def move_file(file):
    dir_names = ["Pictures", "Documents", "Videos", "Music"]

    for dir_name in dir_names:
        ext = "." + file.split(".")[-1]  # File extension
        src = os.path.join(src_path, file)  # source path
        des = os.path.join(ext_des[dir_name]["des"], file)  # destination path
        des_files = os.listdir(ext_des[dir_name]["des"]) # Files in destination folder
        same_dir = os.path.samefile(src_path, ext_des[dir_name]["des"])
        if ext in ext_des[dir_name]["ext"] and not same_dir: # if the file extension is in the destination folder
            if file in src_files and file in des_files: # if the file is a duplicate
                modified_file = modify_duplicate(file, des_files)
                des = os.path.join(ext_des[dir_name]["des"], modified_file)
                os.rename(src, des)
                print(f"{src}  ->  {ext_des[dir_name]['des']} (duplicate)")
            else:
                os.rename(src, des)  # Moves file to appropriate folder
                print(f"{src}  ->  {ext_des[dir_name]['des']}")

            global files_moved
            files_moved += 1


def move_all_files():
    for file in src_files:
        move_file(file)
    print(f"{files_moved} Files Reorganized.")


user_dir = os.path.join(os.path.expanduser("~"))  # User's Directory

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
src_files = os.listdir(src_path)
move_all_files()
