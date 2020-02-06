from datetime import datetime, time
from os import path
from typing import Dict
from usage_stats import UsageStats
from abc import abstractmethod


class AudioFile:
    """Represents an audio file in a music player

    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nicholas Janus(A01179897).
    """

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str):
        """Create a new audio instance"""
        if not isinstance(title, str):
            raise ValueError("title of the song must be a string")
        if not isinstance(artist, str):
            raise ValueError("the artist must be a string")
        if not self.set_runtime(runtime):
            raise ValueError("the runtime must be in the format hh:mm:ss")
        if not path.exists(pathname + filename):
            raise ValueError("path doesn't exist")
        self._title = title
        self._artist = artist
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
        """plays the audo file"""
        self._usage.increment_usage_stats()

    @abstractmethod
    def get_description(self) -> str:
        """returns a description of the audio file"""
        pass

    def get_location(self) -> str:
        """ returns location of audio file """
        return self._pathname + self._filename

    def get_usage_stats(self) -> UsageStats:
        """returns stats about audio file"""
        return self._usage

    @abstractmethod
    def meta_data(self) -> Dict:
       pass

    def get_play_count(self):
        return self._usage.play_count

    def set_runtime(self, runtime: str) -> bool:
        """sets runtime if valid and returns True, if not returns False"""
        time_formats = ['%S', '%M:%S','%H:%M:%S']
        try:
            self._runtime = datetime.strptime(runtime, time_formats[runtime.count(":")]).time()
            return True
        except ValueError:
            return False
