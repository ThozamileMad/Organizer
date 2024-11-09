# File Organizer Script

This Python script automatically sorts and moves files in a specified directory into their correct folders based on their file extensions (e.g., MP3 files are moved to the "Music" directory). If duplicates are found, the script renames them by adding a number to the filename.

## Features

- **Automatic Sorting**: Organizes files into "Pictures", "Videos", "Documents", and "Music" based on their file extension.
- **Duplicate Handling**: If a file with the same name already exists in the destination, it renames the file by adding a number to ensure uniqueness.
- **Customizable**: Easily adjust directories or file types for different use cases.

## How It Works

1. The script scans the specified source directory for files.
2. Files are moved to the appropriate destination directory based on their extension (e.g., `.jpg` files go to "Pictures", `.mp3` files go to "Music").
3. If a file with the same name already exists in the destination folder, it is renamed by appending a unique number.

## Requirements

- Python 3.x

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    ```

2. Navigate to the project folder:
    ```bash
    cd file-organizer
    ```

3. Ensure you have Python installed.

## Usage

1. Run the script:
    ```bash
    python organize_files.py
    ```

2. Enter the path of the target directory when prompted.

    Example:
    ```bash
    Please Enter The Path of The Target Directory: /path/to/your/folder
    ```

3. The script will move files to their respective directories (e.g., `Pictures`, `Videos`, `Documents`, `Music`).

## Customization

- You can easily adjust the source and destination directories by modifying the `ext_des` dictionary in the script.
- Add or remove file extensions to tailor the script to your needs.

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork the repository, submit issues, or create pull requests if you have suggestions or improvements!

---

**Note**: Make sure the `src_path` is a valid directory path before running the script. The script will organize files within that directory based on their extensions and move them to the appropriate folders.
