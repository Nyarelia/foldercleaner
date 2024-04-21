import shutil
import os
import random
import string
from tkinter.filedialog import askopenfilename

IMG_FOLDER = 'Images/'
VID_FOLDER = 'Videos/'
TOR_FOLDER = 'Torrents/'
COMPR_FOLDER = 'Compressed/'
EXEC_FOLDER = 'Executables/'
MISC_FOLDER = 'Miscellaneous/'
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.webm', '.mpg')
TORRENT_EXTENSIONS = ('.torrent',)
EXECUTABLE_EXTENSIONS = ('.exe', '.msi')
COMPRESSED_EXTENSIONS = ('.zip', 'rar', '7z')


def default_folders():
    folders = [IMG_FOLDER, VID_FOLDER, TOR_FOLDER, COMPR_FOLDER, EXEC_FOLDER, MISC_FOLDER]
    return folders


def get_credentials():
    username = os.getlogin()
    default_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    return default_path




def check_for_duplicates(existing_file):
    try:
        (filename, extension) = os.path.splitext(existing_file)
        renaming = False
        if os.path.exists(existing_file):
            renaming = True
        while renaming:
            new_file_name = filename + '_copy' + extension
            if os.path.exists(new_file_name):
                new_file_name = filename + '_copy' + extension
            os.rename(existing_file, new_file_name)
            renaming = False
    except Exception as e:
        print("An error occurred:", e)


def default_folder_query():
    user_answer = input(f'Targeting folder: {path}\nIs this the correct folder? y/n:').lower().strip()
    return user_answer


def create_directories(folder):
    for folder in folder:
        ensure_directory_exists(os.path.join(path, folder))


def ensure_directory_exists(folder):
    os.makedirs(os.path.join(path, folder), exist_ok=True)


def greeting():
    name = os.getlogin()
    print(f'Hello {name}, let\'s get organized!')


def filter_files_based_on_extension(directory, extensions):
    return [file for file in os.listdir(directory) if file.lower().endswith(extensions)]

def move_files(files, start_directory, destination, sub_folder):
    for file in files:
        old_path = path
        new_path = os.path.join(path, sub_folder, file)
        shutil.move(old_path, new_path)

path = get_credentials()

def main_loop():
    greeting()
    files_left = True
    while files_left:




main_loop()

#
#
#
#
# images = filter_files_based_on_extension(START_DIRECTORY, IMAGE_EXTENSIONS)
# videos = filter_files_based_on_extension(START_DIRECTORY, VIDEO_EXTENSIONS)
# torrents = filter_files_based_on_extension(START_DIRECTORY, TORRENT_EXTENSIONS)
# executables = filter_files_based_on_extension(START_DIRECTORY, EXECUTABLE_EXTENSIONS)
# compressed_files = filter_files_based_on_extension(START_DIRECTORY, COMPRESSED_EXTENSIONS)
# # should be loop/function but am lazy
# move_files(images, START_DIRECTORY, END_DIRECTORY, IMAGE_SUB_FOLDER)
# move_files(videos, START_DIRECTORY, END_DIRECTORY, VIDEO_SUB_FOLDER)
# move_files(torrents, START_DIRECTORY, END_DIRECTORY, TORRENT_SUB_FOLDER)
# move_files(executables, START_DIRECTORY, END_DIRECTORY, EXECUTABLE_SUB_FOLDER)
# move_files(compressed_files, START_DIRECTORY, END_DIRECTORY, COMPRESSED_SUB_FOLDER)
