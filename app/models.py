from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies' 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(500))
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime)

    def __init__(self,title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now()

        

    # def is_authenticated(self):
    #     return True
    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)