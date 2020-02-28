from song import Song
from podcast import Podcast
from playlist import PlayList
from typing import List
import os
import eyed3
from math import floor


class AudioLibrary:
    """
        Creates instance of an audio library
        Authors: Anmol Anand(A01174846), Felix Ruttan(A01070306), 
        Nicholas Janus(A01179897)
    """

    def __init__(self):
        """constructor for instance of audio library"""
        self._songs = []
        self._playlists = []
        self._podcasts = []

    def add_song(self, song: Song):
        """adds song to library"""
        if not isinstance(song, Song):
            raise ValueError("argument given is not a Song object")

        self._songs.append(song)

    def add_podcast(self, podcast: Podcast):
        """adds podcast to library"""
        if not isinstance(podcast, Podcast):
            raise ValueError("argument given is not a Podcast object")
        self._podcasts.append(podcast)

    def add_playlist(self, playlist: PlayList):
        """adds playlist to library"""
        if not isinstance(playlist, PlayList):
            raise ValueError("argument given is not a PlayList object")
        self._playlists.append(playlist)

    def get_song_list(self) -> List:
        """returns the list of songs in the library"""
        return self._songs

    def get_podcast_list(self) -> List:
        """returns the list of podcasts in the library"""
        return self._podcasts

    def get_playlist_list(self) -> List:
        """returns the list of playlists in the library"""
        return self._playlists

    def remove_song(self, song: Song):
        """removes song from library"""
        if not isinstance(song, Song):
            raise ValueError("argument given is not a Song object")
        self._songs.remove(song)

    def remove_podcast(self, podcast: Podcast):
        """removes podcast from library"""
        if not isinstance(podcast, Podcast):
            raise ValueError("argument given is not a Podcast object")
        self._podcasts.remove(podcast)

    def remove_playlist(self, playlist: PlayList):
        """removes playlist from library"""
        if not isinstance(playlist, PlayList):
            raise ValueError("argument given is not a PlayList object")
        self._playlists.remove(playlist)

    def number_of_songs(self) -> int:
        """returns the number of songs in the library"""
        return len(self._songs)

    def number_of_podcasts(self) -> int:
        """returns the number of podcasts in the library"""
        return len(self._podcasts)

    def number_of_playlists(self) -> int:
        """returns the number of playlists in the library"""
        return len(self._playlists)

    def search_song(self, search_for: str) -> Song:
        """search library for specific song using regex, when we know regex"""
        raise NotImplementedError

    def search_podcast(self, search_for: str) -> Podcast:
        """search library for specific podcast, using regex, when we know regex"""
        raise NotImplementedError

    def search_playlist(self, search_for: str) -> PlayList:
        """search library for specific playlist, using regex, when we know regex"""
        raise NotImplementedError

    def load(self, dir_path: str):
        """creates song objects for all mp3 files in a directory and adds them to library"""

        song_list = os.listdir(dir_path)

        for song in song_list:
            temp_song_path = os.path.join(os.getcwd(), dir_path, song)
            temp_song_tags = AudioLibrary.__get_song_info(temp_song_path)
            temp_song_object = Song(temp_song_tags['title'], temp_song_tags['artist'],
                                    temp_song_tags['album'], str(temp_song_tags['runtime']),
                                    os.path.join(os.getcwd(), dir_path), song,
                                    temp_song_tags['genre'].name)

            self.add_song(temp_song_object)

    @classmethod
    def __get_song_info(cls, song_path: str):
        """returns the details of the song using the eyed3 module"""

        mp3_file = eyed3.load(song_path)

        tags = {'title': '', 'artist': '', 'album': '', 'genre': ''}

        for field in tags.keys():
            value = getattr(mp3_file.tag, field)
            tags[field] = value

        runtime_secs = mp3_file.info.time_secs
        runtime_mins = int(runtime_secs // 60)

        tags['runtime'] = str(runtime_mins) + ':' + str(floor(runtime_secs) - (runtime_mins * 60))

        return tags
