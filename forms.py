"""Forms for playlist app."""

from wtforms import SelectField, StringField, IntegerField, TextAreaField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name", validators=[InputRequired()])
    Songs = StringField(
        "Select the songs", validators=[Optional()]
    )


    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    name = StringField("Song Name", validators=[InputRequired()])
    author = StringField("Author", validators=[InputRequired()])
    Date_Posted = StringField("Date Published", validators=[Optional()])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE




class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
