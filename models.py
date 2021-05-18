"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    songs = db.relationship(
        'PlaylistSong', backref='playlist'

    )

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    Playlistsong = db.relationship('PlaylistSong', backref='song')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'PlayListSong'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists"), primary_key=True, unique=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs'), primary_key=True)

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
