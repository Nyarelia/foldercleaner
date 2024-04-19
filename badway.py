import shutil
import os

STARTING_LOCATION = 'C:/Users/Sonia/Downloads'
END_LOCATION = 'F:/BrowserDownloads/'

image_location = 'Images/'
video_location = 'Videos/'
torrent_location = 'Torrents/'

images = [f for f in os.listdir(STARTING_LOCATION) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
videos = [f for f in os.listdir(STARTING_LOCATION) if f.lower().endswith(('.mp4', '.avi', '.mov', '.webm', '.mpg'))]
torrents = [f for f in os.listdir(STARTING_LOCATION) if f.lower().endswith('.torrent')]
executables = [f for f in os.listdir(STARTING_LOCATION) if f.lower().endswith(('.exe', '.msi'))]
compressed_files = [f for f in os.listdir(STARTING_LOCATION) if f.lower().endswith(('.zip', 'rar'))]

old_path = os.path.join(STARTING_LOCATION, image)
for image in images:
    new_path = os.path.join(END_LOCATION, image_location, image)
    shutil.move(old_path, new_path)

for video in videos:
    old_path = os.path.join(STARTING_LOCATION, video)
    new_path = os.path.join(END_LOCATION, video_location, video)
    shutil.move(old_path, new_path)

for torrent in torrents:
    old_path = os.path.join(STARTING_LOCATION, torrent)
    new_path = os.path.join(END_LOCATION, torrent_location, torrent)
    shutil.move(old_path, new_path)

for executable in executables:
    old_path = os.path.join(STARTING_LOCATION, executable)
    new_path = os.path.join(END_LOCATION, executable)
    shutil.move(old_path, new_path)

for compressed_file in compressed_files:
    old_path = os.path.join(STARTING_LOCATION, compressed_file)
    new_path = os.path.join(END_LOCATION, compressed_file)
    shutil.move(old_path, new_path)

