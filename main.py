import os

# Function to handle duplicate file names and modify them if needed
def modify_duplicate(file, des_lst):
    segs = file.split(".")  # Split the file name by the extension
    seg = segs[0]  # The name part of the file (before the extension)

    nums = [f"{num + 1}" for num in range(100)]  # List of possible numeric suffixes

    # Check if the file name contains numeric suffixes and remove them to get the base name
    if len(seg) >= 3:
        if f"{seg[-2]}" in nums:
            seg = seg[:-3]

    if len(seg) >= 4:
        if f"{seg[-3]}{seg[-2]}" in nums:
            seg = seg[:-4]

    if len(seg) >= 5:
        if f"{seg[-4]}{seg[-3]}{seg[-2]}" in nums:
            seg = seg[:-5]

    # Create a list of existing files in the destination that match the file extension
    lst = [file for file in des_lst if segs[1] in file]
    # Replace parentheses with asterisks to avoid issues in naming
    new_lst = [item.replace("(", "*").replace(")", "*") for item in lst if seg in item]

    # List to store duplicate numbers found in the file names
    dup_nums = []
    for file in new_lst:
        try:
            mod_file = file.split("*")
            dup_nums.append(int(mod_file[-2]))  # Extract numeric suffix from file name
        except IndexError:
            pass

    # Find the next available number for the duplicate file
    file_num = 1
    for num in range(len(dup_nums)):
        min_num = min(dup_nums)  # Get the smallest number
        if min_num + 1 not in dup_nums:  # If the next number is available
            file_num = min_num + 1
        else:
            dup_nums.remove(min_num)  # Remove used number

    # Return the new modified file name with the numeric suffix
    new_file = seg + f"({file_num})" + "." + segs[-1]
    return new_file


# Function to move a single file to the appropriate directory based on its extension
def move_file(file):
    # Get the list of destination directories that exist
    dir_names = [key for key in ext_des if os.path.exists(ext_des[key]["des"])]
    
    # Loop through each directory and check if the file belongs there
    for dir_name in dir_names:
        ext = "." + file.split(".")[-1]  # Get the file extension
        src = os.path.join(src_path, file)  # Source file path
        des = os.path.join(ext_des[dir_name]["des"], file)  # Destination file path
        des_files = os.listdir(ext_des[dir_name]["des"])  # Files already in destination folder
        same_dir = os.path.samefile(src_path, ext_des[dir_name]["des"])  # Check if source and destination are the same
        
        # If the file extension matches the destination folder's allowed extensions and is not in the same directory
        if ext in ext_des[dir_name]["ext"] and not same_dir:
            # If the file is a duplicate, modify its name to avoid conflicts
            if file in src_files and file in des_files:
                modified_file = modify_duplicate(file, des_files)
                des = os.path.join(ext_des[dir_name]["des"], modified_file)
                os.rename(src, des)  # Rename (move) the file to the destination
                print(f"{src}  ->  {ext_des[dir_name]['des']} (duplicate)")
            else:
                os.rename(src, des)  # Move the file to the appropriate folder
                print(f"{src}  ->  {ext_des[dir_name]['des']}")

            global files_moved  # Global counter to track the number of moved files
            files_moved += 1


# Function to move all files from the source directory
def move_all_files():
    for file in src_files:
        move_file(file)  # Call move_file function for each file
    print(f"{files_moved} Files Reorganized.")  # Print total files moved


# Get the user's directory and define the destination paths for each file type
user_dir = os.path.join(os.path.expanduser("~"))  # User's home directory

# Define file extensions and corresponding directories for categorization
ext_des = {
    "Pictures": {
        "ext": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],  # Allowed picture file extensions
        "des": os.path.join(user_dir, "Pictures")  # Destination directory for pictures
    },
    "Videos": {
        "ext": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm", ".mpeg"],  # Allowed video file extensions
        "des": os.path.join(user_dir, "Videos")  # Destination directory for videos
    },
    "Documents": {
        "ext": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".md"],  # Allowed document file extensions
        "des": os.path.join(user_dir, "Documents")  # Destination directory for documents
    },
    "Music": {
        "ext": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".alac"],  # Allowed music file extensions
        "des": os.path.join(user_dir, "Music")  # Destination directory for music
    }
}

# Set the current working directory and request user input for the source path
os.chdir("/")  # Change to the root directory
src_path = input("Please Enter The Path of The Target Directory: ")  # Source directory input from user
files_moved = 0  # Initialize counter for moved files
src_files = os.listdir(src_path)  # Get a list of files in the source directory

# Call the function to move all files
move_all_files()
