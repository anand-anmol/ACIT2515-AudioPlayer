from flask import Flask, request
from song_manager import SongManager
from song import Song
import json
import random

app = Flask(__name__)

song_mgr = SongManager('song_db.sqlite')


@app.route('/song', methods=['POST'])
def add_song():
    """ Add a song to the database """
    content = request.json

    if not 'genre' in content.keys():
        content['genre'] = None

    try:
        song = Song(content['title'],
                    content['artist'],
                    content['album'],
                    content['runtime'],
                    content['file_location'],
                    content['genre'],
                    )
        song_mgr.add_song(song)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/play_song/<string:song_number_in_listbox>', methods=['POST'])
def play_song(song_number_in_listbox):
    """ Updates the play count and last played values in the database """

    songs = song_mgr.get_all_songs()

    try:
        song_mgr.play_song(songs[int(song_number_in_listbox)])
    except IndexError:
        print(f"Song {song_number_in_listbox} does not exist")


    response = app.response_class(
            status=200,
            mimetype='application/json'
        )

    return response


@app.route('/song/<string:song_id>', methods=['GET'])
def get_song(song_id):
    """ Get a song from the database """
    try:
        song = song_mgr.get_song(song_id)
        if song is None:
            raise ValueError(f"song {song_id} does not exist")

        response = app.response_class(
            status=200,
            response=json.dumps(song.meta_data()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response

@app.route('/song/name/<string:song_title>', methods=['GET'])
def get_song_by_name(song_title):
    """ Get a song from the database """
    try:
        song = song_mgr.get_song_by_name(song_title)
        if song is None:
            raise ValueError(f"song {song_title} does not exist")

        response = app.response_class(
            status=200,
            response=json.dumps(song.meta_data()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response

@app.route('/song/random', methods=['GET'])
def random_song():
    """ Return a random song from the database """
    try:
        names = song_mgr.get_all_songs()

        if len(names) > 0:
            id = random.randint(0, len(names) - 1)
            random_song = names[id]
        else:
            raise ValueError("No songs in DB")

        response = app.response_class(
            status=200,
            response=json.dumps(random_song.meta_data()),
            mimetype='application/json'
        )
        return response
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response


@app.route('/song/<string:song_number_in_listbox>', methods=['DELETE'])
def delete_song(song_number_in_listbox):
    """ Delete a song from the DB   """

    songs = song_mgr.get_all_songs()

    try:
        song_mgr.delete_song(songs[int(song_number_in_listbox)])
        response = app.response_class(
            status=200
        )
    except IndexError:
        print(f"Song {song_number_in_listbox} does not exist")

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )

    return response


@app.route('/song/names', methods=['GET'])
def get_all_names():
    """ Return a list of all song names    """
    names = song_mgr.get_all_songs()

    response = app.response_class(
        status=200,
        response=json.dumps([s.meta_data() for s in names]),
        mimetype='application/json'
    )

    return response


@app.route('/song/<string:song_number_in_listbox>', methods=['PUT'])
def update_song(song_number_in_listbox):
    """ Update the song information  """
    content = request.json

    songs = song_mgr.get_all_songs()

    try:
        song = songs[int(song_number_in_listbox)]
    except IndexError:
        print(f"Song {song_number_in_listbox} does not exist")

    if not 'genre' in content.keys():
        content['genre'] = None

    try:
        song.genre = content['genre']
        song.rating = content['rating']
        song_mgr.update_song(song)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response


@app.route('/song/all', methods=['DELETE'])
def delete_all_songs():
    """ Delete a song from the DB   """
    try:
        song_mgr.delete_all_songs()
        response = app.response_class(status=200)
    except ValueError as e:
        response = app.response_class(response=str(e), status=404)
    return response


if __name__ == "__main__":
    app.run(debug=True)
