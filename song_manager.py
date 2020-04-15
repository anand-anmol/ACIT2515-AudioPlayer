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
