import os
import fnmatch
import id3reader_p3 as id3reader


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song

#
# album_list = find_albums("music", input("Artist please: "))
# song_list = find_songs(album_list)
# #
# # for a in album_list:
# #     print(a)
#
# for s in song_list:
#     print(s)


def music_search(start_dir, extension):
    for path, directories, files in os.walk(start_dir):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


music_files = music_search("music", 'emp3')

error_list = []
for f in music_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value("performer"),
            id3r.get_value("album"),
            id3r.get_value("track"),
            id3r.get_value("song")
        ))
    except OSError:
        error_list.append(f)

for error_file in error_list:
    print(error_file)