from datetime import datetime
from os import path
from typing import Dict
from usage_stats import UsageStats
from abc import abstractmethod


class Audio:
    """Represents an audio file in a music player

    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nicholas Janus(A01179897).
    """

    def __init__(self, title: str, artist: str, album: str, runtime: str, pathname: str, filename: str):
        """Create a new audio instance"""
        if not isinstance(title, str):
            raise ValueError("title of the song must be a string")
        if not isinstance(artist, str):
            raise ValueError("the artist must be a string")
        if not isinstance(runtime, str):
            raise ValueError("the runtime must be in the format hh:mm:ss")
        if not path.exists(pathname + filename):
            raise ValueError("path doesn't exist")
        self._title = title
        self._artist = artist
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

    @abstractmethod
    def get_description(self) -> str:
        """returns a description of the song"""
        pass

    def get_location(self) -> str:
        return self._pathname + self._filename

    def get_usage_stats(self) -> UsageStats:
        return self._usage

    @abstractmethod
    def meta_data(self) -> Dict:
       pass

    def get_play_count(self):
        return self._usage.play_count
