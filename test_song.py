from song import Song
from song_manager import SongManager


def main():
    song1 = Song('The Calling', 'Artist', 'AlbumABC', "3:02", "./test_songs/The Calling  - Angelwing.mp3")
    song_manager = SongManager("song_db.sqlite")
    song_manager.add_song(song1)


if __name__ == '__main__':
    main()
