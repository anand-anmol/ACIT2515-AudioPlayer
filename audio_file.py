from datetime import datetime
from os import path
from typing import Dict
from usage_stats import UsageStats


class Audio:
    """Represents an audio file in a music player

    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nick Janus(A01179897).
    """

    def __init__(self, title: str, artist: str, album: str, runtime: str, pathname: str, filename: str):
        """Create a new audio instance"""
        if not isinstance(title, str):
            raise ValueError("title of the song must be a string")
        if not isinstance(artist, str):
            raise ValueError("the artist must be a string")
        if not isinstance(album, str):
            raise ValueError("the name of the album must be a string")
        if not isinstance(runtime, str):
            raise ValueError("the runtime must be in the format hh:mm:ss")
        if not path.exists(pathname + filename):
            raise ValueError("path doesn't exist")
        self._title = title
        self._artist = artist
        self._album = album
        self._runtime = runtime
        self._rating = None
        self._pathname = pathname
        self._filename = filename
        self._usage = UsageStats(datetime.now())

    @property
    def rating(self) -> float:
        """gets value for user ratings"""
        return self._rating

    @rating.setter
    def rating(self, value: float):
        """sets the value of user ratings"""
        self._rating = value

    def update_usage_stats(self):
        """plays the song"""
        self._usage.increment_usage_stats()

    def get_description(self) -> str:
        """returns a description of the song"""
        if self._rating is None:
            song_description = "{} by {} from the album {} added on {}. Runtime is {}"\
            .format(self._title, self._artist,self._album,self._usage.date_added,self._runtime)
        else:
            song_description = "{} by {} from the album {} added on {}. Runtime is {}. User Rating is {}"\
                .format(self._title, self._artist, self._album,self._usage.date_added, self._runtime, self._rating)
        return song_description

    def get_location(self) -> str:
        return self._pathname + self._filename

    def get_usage_stats(self) -> UsageStats:
        return self._usage

    def meta_data(self) -> Dict:
        meta_data_dict = {
            'title': self._title, 
            'artist': self._artist, 
            'album': self._album,
            'date_added': self._usage.date_added, 
            'runtime': self._runtime, 
            'pathname': self._pathname,
            'filename': self._filename, 
            'play_count': self._usage.play_count,
            'last_played': self._usage.last_played, 
            'rating': self._rating}
        return meta_data_dict

    def get_play_count(self):
        return self._usage.play_count
