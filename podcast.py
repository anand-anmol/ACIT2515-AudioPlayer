from audio_file import AudioFile
from datetime import datetime, time
from typing import Dict
from usage_stats import UsageStats

class Podcast(AudioFile):
    """Represents an audio file in an audio player
    
    Author: Anmol Anand(A01174846)
    """

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str, series:str, season:str, progress:time, episode_number:int= None, episode_date:datetime=None):
        """Creates an instance of a Podcast"""

        if episode_date is not None:
            if not isinstance(episode_date, datetime):
                raise ValueError("episode date is not a datetime object")
        if not isinstance(series, str):
            raise ValueError("series is not a string")
        if not isinstance(season, str):
            raise ValueError("season is not a string")
        if episode_number is not None:
            if not isinstance(episode_number, int):
                raise ValueError("episode number is not an integer")
        if not isinstance(progress, time):
            raise ValueError("progress is not a time object")

        super().__init__(title, artist, runtime, pathname, filename)
        self._series = series
        self._season = season
        self._episode_number = episode_number
        self._episode_date = episode_date
        self._progress = progress
        self._usage = UsageStats(datetime.now())

    @property
    def series(self) -> str:
        """returns the series for the podcast"""
        return self._series

    @series.setter
    def series(self, series):
        self._series = series

    @property
    def season(self) -> str:
        """returns the season of the podcast"""
        return self._season
    
    @season.setter
    def season(self, season):
        self._season = season

    @property
    def episode_number(self) -> int:
        """returns the episode number for the season"""
        return self._episode_number

    @episode_number.setter
    def episode_number(self, episode_number):
        self._episode_number = episode_number

    def get_description(self) -> str:
        """returns a string with a description of the podcast"""
        
        if self._episode_number is None and self._season is None:
            description = "{}: {}, {} ({} mins)".\
                    format(self._series, self._title, self._episode_date, self._runtime.minute)

        elif self._episode_number is None:
            description = "{}: {}, {}, Season {} ({} mins)".\
                    format(self._series, self._title, self._episode_date, self._season, self._runtime.minute)

        else:
            description = "{}: {}, {}, Season {} Episode {} ({} mins)".\
                    format(self._series, self._title, self._episode_date, self._season, self._episode_number, self._runtime.minute)

        return description

    def get_progress(self) -> time:
        """returns a time object that shows the current timestamp the user is at"""

        return self._progress

    def meta_data(self) -> Dict:
        """returns a dictionary with meta data about the podcast"""
        
        meta_data_dict = {
                            'title': self._title,
                            'artist': self._artist,
                            'series': self._series,
                            'season': self._season,
                            'episode_number': self._episode_number,
                            'episode_date': self._episode_date,
                            'progress': self._progress,
                            'date_added': self._usage.date_added,
                            'runtime': self._runtime, 
                            'pathname': self._pathname,
                            'filename': self._filename, 
                            'play_count': self._usage.play_count,
                            'last_played': self._usage.last_played, 
                            'rating': self._rating
                         }
        
        return meta_data_dict