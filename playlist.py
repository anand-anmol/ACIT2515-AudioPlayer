from usage_stats import UsageStats
from datetime import datetime
from song import Song
from typing import List


class PlayList:
    """
    a playlist for the music player
    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nick Janus(A01179897).
    """

    def __init__(self, play_list_name: str, description: str):
        """creates a playlist object"""
        self._name = play_list_name
        self._description = description
        self._usage = UsageStats(datetime.now())
        self._playlist = []

    @property
    def name(self):
        """getter for the playlist name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """setter for the playlist name"""
        self._name = new_name

    @property
    def description(self):
        """getter for the playlist description"""
        return self._description

    @description.setter
    def description(self, new_description):
        """setter for the playlist description"""
        self._description = new_description

    def add_song(self, song: Song, posn: int = None):
        """add a song to the playlist"""
        if posn is not None:
            if len(self._playlist) > posn >= 0:
                self._playlist.insert(posn, song)
            else:
                raise ValueError("Position", posn, "is not available for", self._name)
        else:
            self._playlist.append(song)

    def remove_song(self, song: Song):
        """removes a song from the playlist"""
        try:
            self._playlist.remove(song)
        except ValueError:
            print(song, "is not in the playlist", self._name)

    def move_song(self, song: Song, posn: int):
        """changes the position of the song in the playlist"""
        if len(self._playlist) > posn >= 0:
            try:
                self._playlist.insert(posn, self._playlist.pop(self._playlist.index(song)))
            except ValueError:
                print(song, "is not in the playlist", self._name)
        else:
            raise ValueError("Position", posn, "is not available for", self._name)

    def list_songs(self) -> List:
        """returns a list of the songs in the playlist"""
        song_list = []
        for i in self._playlist:
            (song_list.append(
                "{}{}{}{}{}".\
                    format(str(self._playlist.index(i) + 1), i._title.ljust(20), i._artist.ljust(20),
                                    i._album.ljust(20), i._runtime.ljust(20))))
        return song_list

    def get_song_by_position(self, posn: int) -> Song:
        """returns a song object corresponding to the posn specified"""

        if len(self._playlist) > posn >= 0:
            return self._playlist[posn]
        else:
            raise ValueError("Position", posn, "is not available for", self._name)

    def find_song(self, title: str = None, artist: str = None, album: str = None) -> int or None:
        """Returns a song that matches the title, artist and/or album"""

        if title is not None:
            by_title = set([self._playlist.index(song) for song in self._playlist if song._title == title])
        else:
            by_title = set([i for i in range(len(self._playlist))])
        if album is not None:
            by_album = set([self._playlist.index(song) for song in self._playlist if song._album == album])
        else:
            by_album = set([i for i in range(len(self._playlist))])
        if artist is not None:
            by_artist = set([self._playlist.index(song) for song in self._playlist if song._artist == artist])
        else:
            by_artist = set([i for i in range(len(self._playlist))])
        possible_songs = list(by_title.intersection(by_album, by_artist))

        if len(possible_songs) > 0:
            return possible_songs[0]
        else:
            return None

    def number_of_songs(self) -> int:
        """returns the number of songs stored in the playlist"""

        return len(self._playlist)

    def update_usage_stats(self):
        """updates the play count and the last played data in the UsageStats object"""

        self._usage.increment_usage_stats()

    def get_usage_stats(self) -> UsageStats:
        """returns the UsageStats object for the playlist"""

        return self._usage
