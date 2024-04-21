import os
import shutil

# Directories
FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov', '.webm', '.mpg'],
    'Executables': ['.exe', '.msi'],
    'Compressed': ['.zip', '.rar', '7z']
}

MISC_FOLDER = 'Miscellaneous/'


def ensure_directory_exists(folder):
    os.makedirs(os.path.join(path, folder), exist_ok=True)


def get_credentials():
    username = os.getlogin()
    default_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    return default_path


def greeting():
    name = os.getlogin()
    print(f'Hello {name}, let\'s get organized!')


def filter_files_based_on_extension(dir_, ext):
    return [file for file in os.listdir(dir_) if file.lower().endswith(ext)]


def move_files(files, start_directory, sub_folder):
    for file in files:
        old_path = os.path.join(start_directory, file)
        new_path = os.path.join(start_directory, sub_folder, file)
        shutil.move(old_path, new_path)


path = get_credentials()


def move_to_misc(start_directory, valid_extensions, sub_folder):
    for filename in os.listdir(start_directory):
        # Skip if filename is a key in FOLDERS dictionary
        if filename in FOLDERS.keys():
            continue
        _, ext = os.path.splitext(filename)
        if ext not in valid_extensions and os.path.isfile(os.path.join(start_directory, filename)):
            shutil.move(
                os.path.join(start_directory, filename),
                os.path.join(start_directory, sub_folder, filename)
            )


def main_loop():
    greeting()

    # Ensure directories exist
    for key in FOLDERS.keys():
        ensure_directory_exists(os.path.join(path, key))

    ensure_directory_exists(os.path.join(path, MISC_FOLDER))

    # List all valid extensions
    valid_extensions = [ext for extensions in FOLDERS.values() for ext in extensions]

    # Move files to respective directories
    for folder, extensions in FOLDERS.items():
        for extension in extensions:
            files_to_move = filter_files_based_on_extension(path, extension)
            move_files(files_to_move, path, folder)

    # Move remaining files to Miscellaneous directory
    move_to_misc(path, valid_extensions, MISC_FOLDER)


main_loop()
