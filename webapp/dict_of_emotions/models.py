from webapp.db import db

class Articles(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<Articles {} {}>'.format(self.title, self.url)
        
class Text_Record(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=False)
        title = db.Column(db.String, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<Text_Record {} {}>'.format(self.title)
        
class Exercises(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<Exercises {} {}>'.format(self.title, self.url)