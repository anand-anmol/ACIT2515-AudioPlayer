from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from song import Song


class SongManager:

    def __init__(self, db_filename):
        """ Initializes the list of songs """

        if db_filename is None or db_filename == "":
            raise ValueError("Invalid Database File")

        engine = create_engine('sqlite:///' + db_filename)

        # Bind the engine to the metadata fo the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add_song(self, song):
        """ Adds a new song """

        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        session.add(song)
        session.commit()

        song_id = song.id

        session.close()

        return song_id

    def update_song(self, song):
        """ Update existing song to match song_upd """
        if song is None or not isinstance(song, Song):
            raise ValueError("Invalid Song Object")

        session = self._db_session()

        existing_song = session.query(Song).filter(
                Song.id == song.id).first()
        if existing_song is None:
            raise ValueError(f"Song {song.id} does not exist")

        existing_song.update(song)

        session.commit()
        session.close()

    def get_song(self, id):
        """ Return song object matching ID"""
        if id is None or type(id) != str:
            raise ValueError("Invalid Song ID")

        session = self._db_session()

        song = session.query(Song).filter(
                Song.id == id).first()

        session.close()

        return song

    def delete_song(self, id):
        """ Delete a song from the database """
        if id is None or type(id) != str:
            raise ValueError("Invalid Song ID")

        session = self._db_session()

        song = session.query(Song).filter(
                Song.id == id).first()
        if song is None:
            session.close()
            raise ValueError("Song does not exist")

        session.delete(song)
        session.commit()

        session.close()

    def get_all_songs(self):
        """ Return a list of all songs in the DB """
        session = self._db_session()

        all_songs = session.query(Song).all()

        session.close()

        return all_songs

    def delete_all_songs(self):
        """ Delete all songs from the database """

        session = self._db_session()
        session.query(Song).delete()
        session.commit()
        session.close()