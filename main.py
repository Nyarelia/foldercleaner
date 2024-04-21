import os
import shutil

IMG_FOLDER = 'Images/'
VID_FOLDER = 'Videos/'
COMPR_FOLDER = 'Compressed/'
EXEC_FOLDER = 'Executables/'
MISC_FOLDER = 'Miscellaneous/'

extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov', '.webm', '.mpg'],
    'Executables': ['.exe', '.msi'],
    'Compressed': ['.zip', 'rar', '7z'],
    'Torrents': ['.torrent']
}


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


def main_loop():
    greeting()
    files_left = True
    while files_left:
        for key in extensions:
            if not os.path.exists(os.path.join(path, key)):
                ensure_directory_exists(os.path.join(path, key))
            for value in extensions[key]:
                move_files(filter_files_based_on_extension(path, value), path, key)
        files_left = False


main_loop()


