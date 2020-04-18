from sqlalchemy import Column, Text
from audio_file import AudioFile
from datetime import datetime, time
from typing import Dict
from usage_stats import UsageStats

class Song(AudioFile):
    """ Models a single song that can be played by an audio player.
    
    Author: Anmol Anand(A01174846), Nicholas Janus(A01179897).
    """

    """ ORM: map db columns to instance variables in this class """
    album = Column(Text)
    genre = Column(Text)
    rating = Column(Text)

    def __init__(self, title: str, artist: str, album: str, runtime: str, file_location: str,  genre: str = None, rating: int = None):
        """Creates an instance of a song"""

        if not isinstance(album, str):
            raise ValueError("album must be a string")
        if genre is not None and isinstance(genre, str):
            self.genre = genre
        else:
            self.genre = None

        super().__init__(title, artist, runtime, file_location)
        self.album = album
        if rating is not None and isinstance(rating, int):
            self.rating = rating
        else:
            self.rating = None
    def get_album(self) -> str:
        """returns the song.album or sets the song.album"""
        return self.album

    def set_album(self, update: str):
        self.album = update

    def get_genre(self) -> str:
        """returns the song.genre or sets the song.genre"""
        return self.genre

    def get_runtime(self) -> str:
        """returns the runtime for the song object"""

        return self.runtime

    def set_genre(self, update: str):
        try:
            if self.genre is not None and update.strip() not in self.genre:
                self.genre += ",", update
            else:
                self.genre = update
        except TypeError:
            print("genre must be string")

    def meta_data(self) -> Dict:
        """returns a dictionary of song meta data"""
        meta_dict = {
            "title": str(self.title),
            "artist": str(self.artist),
            "album": str(self.album),
            "date_added": str(self.date_added),
            "runtime": str(self.runtime),
            "file_location": str(self.file_location),
            "genre": str(self.genre),
            "play_count": str(self.play_count),
            "last_played": str(self.last_played),
            "rating": str(self.rating)
        }
        return meta_dict

    def get_description(self):
        """prints out details about the song object"""
        try:
            song_details = "{} by {} from the album {} added on {}. Runtime is {}." \
                .format(self.title, self.artist, self.album, self._usage._date_added, self.runtime)

            if self._usage.last_played is not None:
                song_details += " Last played on " + str(self._usage.last_played) + "."
            if self.rating is not None:
                song_details += " User rating is " + str(self.rating) + "/5."
        except AttributeError:
            song_details = "Song is missing info, cannot display"

        return song_details

    def play_song(self):
        """ updates the play count and last played values """

        self.play_count += 1
        self.last_played = datetime.now()

    def update(self, object):
        """ updates the instance variables of the song object with the object supplied """

        if isinstance(object, Song):
            self.genre = object.genre
            self.rating = object.rating

    def set_rating(self, update):
        """ setter for the rating of the song """
        self.rating = update
        print(self.rating)