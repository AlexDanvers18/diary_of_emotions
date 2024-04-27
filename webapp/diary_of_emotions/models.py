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
        text_victory  = db.Column(db.String)
        text_curiosity = db.Column(db.String)
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
        
class EmoRecord(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.ForeignKey(User.id))
        emotion_1 = db.Column(db.String)
        emotion_2 = db.Column(db.String)
        emotion_3 = db.Column(db.String)
        emotion_4 = db.Column(db.String)
        emotion_5 = db.Column(db.String)
        emotion_6 = db.Column(db.String)
        emotion_7 = db.Column(db.String)
        emotion_8 = db.Column(db.String)
        emotion_9 = db.Column(db.String)
        emotion_10 = db.Column(db.String)
        emotion_11 = db.Column(db.String)
        emotion_12 = db.Column(db.String)
        emotion_13 = db.Column(db.String)
        emotion_14 = db.Column(db.String)
        emotion_15 = db.Column(db.String)
        emotion_16 = db.Column(db.String)
        emotion_17 = db.Column(db.String)
        emotion_18 = db.Column(db.String)
        emotion_19 = db.Column(db.String)
        emotion_20 = db.Column(db.String)
        emotion_21 = db.Column(db.String)
        emotion_22 = db.Column(db.String)
        emotion_23 = db.Column(db.String)
        emotion_24 = db.Column(db.String)
        emotion_25 = db.Column(db.String)
        emotion_26 = db.Column(db.String)
        emotion_27 = db.Column(db.String)
        emotion_28 = db.Column(db.String)
        emotion_29 = db.Column(db.String)
        emotion_30 = db.Column(db.String)
        emotion_31 = db.Column(db.String)
        emotion_32 = db.Column(db.String)
        emotion_33 = db.Column(db.String)
        emotion_34 = db.Column(db.String)
        emotion_35 = db.Column(db.String)
        emotion_36 = db.Column(db.String)
        emotion_37 = db.Column(db.String)
        emotion_38 = db.Column(db.String)
        emotion_39 = db.Column(db.String)
        emotion_40 = db.Column(db.String)
        emotion_41 = db.Column(db.String)
        emotion_42 = db.Column(db.String)
        emotion_43 = db.Column(db.String)
        emotion_44 = db.Column(db.String)
        emotion_45 = db.Column(db.String)
        published = db.Column(db.DateTime, index=True, default=datetime.now)
        user = relationship('User')

        def __repr__(self):
            return '<Emo_Record {} {}>'.format(self.id, self.published)
        
        