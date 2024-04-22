from sqlalchemy import Column, Integer, String, Date, ForeignKey
from webapp.db import db
from webapp.user.models import User
from sqlalchemy.orm import relationship
from datetime import datetime

class Articles(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<Articles {} {}>'.format(self.title, self.url)
        
class TextRecord(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.ForeignKey(User.id))
        text_situation = db.Column(db.String)
        text_thoughts = db.Column(db.String)
        text_emotions = db.Column(db.String)
        text_bodily_sensations = db.Column(db.String)
        text_result  = db.Column(db.String)
        published = db.Column(db.DateTime, index=True, default=datetime.now)
        user = relationship('User')

        def __repr__(self):
            return '<Text_Record {} {}>'.format(self.id, self.published)
        

class SmileRecord(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.ForeignKey(User.id))
        smile_good = db.Column(db.String)
        smile_crazy = db.Column(db.String)
        smile_neutral = db.Column(db.String)
        smile_agry = db.Column(db.String)
        smile_sad = db.Column(db.String)
        published = db.Column(db.DateTime, index=True, default=datetime.now)
        user = relationship('User')

        def __repr__(self):
            return '<Smile_Record {} {}>'.format(self.id, self.published)
        
        