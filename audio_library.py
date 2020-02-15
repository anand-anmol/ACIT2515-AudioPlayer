from song import Song
from podcast import Podcast
from playlist import PlayList
from typing import List

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
        self._songs.append(song)
    
    def add_podcast(self, podcast: Podcast):
        """adds podcast to library"""
        self._podcasts.append(podcast)

    def add_playlist(self, playlist: PlayList):
        """adds playlist to library"""
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
        self._songs.remove(song)

    def remove_podcast(self, podcast: Podcast):
        """removes podcast from library"""
        self._podcasts.remove(podcast)
    
    def remove_playlist(self, playlist: PlayList):
        """removes playlist from library"""
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