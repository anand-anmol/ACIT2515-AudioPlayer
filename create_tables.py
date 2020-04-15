import sqlite3

conn = sqlite3.connect('song_db.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE song_tbl
          (id INTEGER PRIMARY KEY ASC,
           title TEXT NOT NULL,
           file_location TEXT NOT NULL,
           runtime TIME,
           date_added TEXT NOT NULL,
           play_count INTEGER NOT NULL,
           last_played TEXT,
           rating INTEGER,
           album TEXT,
           genre TEXT,
           artist TEXT NOT NULL)
          ''')

conn.commit()
conn.close()
