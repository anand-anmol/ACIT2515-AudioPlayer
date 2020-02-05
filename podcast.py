from AudioFile import AudioFile
from datetime import datetime, Time
from typing import Dict

class Podcast(AudioFile):
    """Represents an audio file in an audio player
    
    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nicholas Janus(A01179897).
    """

    def __init__(self, series:str, season:str, episode_number:int, episode_date:datetime, progress:Time):
        """Creates an instance of a Podcast"""
        self._series = series
        self._season = season
        self._episode_number = episode_number
        self._episode_date = episode_date
        self._progress = progress

    def get_description() -> str:
        """"""
        pass

    def get_progress() -> Time:
        """"""
        pass

    def meta_data() -> Dict:
        """"""
        pass