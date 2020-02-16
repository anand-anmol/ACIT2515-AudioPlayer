from audio_file import AudioFile
from datetime import datetime, time
from typing import Dict
from usage_stats import UsageStats

class Song(AudioFile):
    """Represents a song subclass of audio file
    
    Author: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nicholas Janus(A01179897).
    """

    def __init__(self, title: str, artist: str, album: str, runtime: str, pathname: str, filename: str,  genre: str = None):
        """Creates an instance of a song"""

        if not isinstance(album, str):
            raise ValueError("album must be a string")
        if genre is not None and isinstance(genre, str):
            self._genre = Song.genre(genre)
        else:
            self._genre = None

        super().__init__(title, artist, runtime, pathname, filename)
        self._album = album

    @property
    def album(self) -> str:
        """returns the song._album or sets the song._album"""
        return self._album

    @album.setter
    def album(self, update: str): 
        self._album = update

    @property
    def genre(self) -> str:
        """returns the song._genre or sets the song._genre"""
        return self._genre

    @genre.setter
    def genre(self, update: str):
        try:
            if self._genre is not None and update.strip() not in self._genre:
                self._genre += ",", update
            else:
                self._genre = update
        except TypeError:
            print("genre must be string")

    def meta_data(self) -> Dict:
        """returns a dictionary of song meta data"""
        meta_dict = {
            "title": str(self._title),
            "artist": str(self._artist),
            "album": str(self._album),
            "date_added": str(self._usage.date_added),
            "runtime": str(self._runtime),
            "pathname": str(self._pathname),
            "filename": str(self._filename),
            "genre": str(self._genre),
            "play_count": str(self._usage.play_count),
            "last_played": str(self._usage.last_played),
            "rating": str(self._rating)
        }
        return meta_dict

    def get_description(self):
        """prints out details about the song object"""
        try:
            song_details = "{} by {} from the album {} added on {}. Runtime is {}." \
                .format(self._title, self._artist, self._album, self._usage._date_added, self._runtime)
            
            if self._usage.last_played is not None:
                song_details += " Last played on " + str(self._usage.last_played) + "."
            if self.rating is not None:
                song_details += " User rating is " + str(self.rating) + "/5."
        except AttributeError:
            song_details = "Song is missing info, cannot display"

        return song_details
