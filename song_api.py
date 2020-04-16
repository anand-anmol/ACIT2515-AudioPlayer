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


@app.route('/song/<string:song_id>', methods=['DELETE'])
def delete_song(song_id):
    """ Delete a song from the DB   """
    try:
        song_mgr.delete_song(song_id)

        response = app.response_class(
            status=200
        )
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


@app.route('/song/<string:song_id>', methods=['PUT'])
def update_song(song_id):
    """ Update the song information  """
    content = request.json

    if not 'genre' in content.keys():
        content['genre'] = None

    try:
        song = song_mgr.get_song(song_id)
        song.title = content['title']
        song.artist = content['artist']
        song.album = content['album']
        song.runtime = content['runtime']
        song.file_location = content['file_location']
        song.genre = content['genre']
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
