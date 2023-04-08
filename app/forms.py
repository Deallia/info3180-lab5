from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class  MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()], 
                        render_kw={"style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    description = TextAreaField('Description',validators=[InputRequired()], 
                        render_kw={"style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
    poster = FileField('Poster' , validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')], 
                        render_kw={ "style": "margin-bottom: 20px;" "box-shadow: 6px 7px 5px -8px #a5a8ac;"})
   