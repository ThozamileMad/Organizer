import os
from pathlib import Path
from time import sleep
from pprint import pprint

class Organizer:
    def __init__(self):
        self.file_extensions = {
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

        root_path = os.path.abspath(Path("/"))
        os.chdir(Path(f"{root_path}/Users"))
        users_dir_lst = os.listdir(os.getcwd())
        self.username = users_dir_lst[1]
        os.chdir(Path(f"{os.getcwd()}/{self.username}"))
        self.main_dir_names = ["Downloads", "Desktop", "Pictures", "Videos", "Music"]
        self.dvpd_dir_dict = {dir_name: os.listdir(Path(f"./{dir_name}")) for dir_name in self.main_dir_names}


    def organize(self, dir_name):
        for filename in self.dvpd_dir_dict[f"{dir_name}"]:
            try:
                file_extension = filename.split('.')[1]
            except IndexError:
                file_extension = "!extensions"

            for k, v in self.file_extensions.items():
                if f".{file_extension}" in v:
                    try:
                        os.rename(Path(f"./{dir_name}/{filename}"), Path(f"./{k}/{filename}"))
                    except FileNotFoundError and FileExistsError:
                        pass


organizer_cls = Organizer()
run = True
while run:
    chosen_directory = input('Please select which folder you would like to reorganize ("Downloads", "Desktop", "Pictures", "Videos", "Music"): ').capitalize()
    if chosen_directory in organizer_cls.main_dir_names:
        organizer_cls.organize(chosen_directory)
        print("\n...")
        sleep(1)
        print("Folder reorganized")
        should_restart = input("\nWould you like to reorganize another folder (yes/no): ").lower()
        if should_restart == "no":
            print("Take Care!")
            run = False
    else:
        print("Invalid Input!!! Please select the correct folder.")
