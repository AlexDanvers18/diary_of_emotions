from sqlalchemy.sql import func
from webapp.diary_of_emotions.models import SmileRecord
from sqlalchemy import desc
from webapp.db import db
from datetime import datetime
from flask_login import current_user
# from db import db_session
from datetime import datetime, timedelta


import locale
import platform

from pathlib import Path
import os
import json


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def parse_date(date_str):
    # date_str = str(date_str)
    # if 'сегодня' in date_str:
    #     today = datetime.now()
    #     date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    # elif 'вчера' in date_str:
    #     yesterday = datetime.now() - timedelta(days=1)
    #     date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return date_str.strftime(f"%d %B %Y в %H:%M")
    except ValueError:
        return datetime.now()
    


def complete_smile_record(user_id):
    
    smiles = db.session.query(SmileRecord).filter_by(user_id=1).all()
    # texts = db.session.query(TextRecord).filter_by(current_user.id).all()
 
    content_file_name = (f'tmp/smile_content_{user_id}.txt')

    # with open(content_file_name, "w", encoding='cp1251') as f:
    with open(content_file_name, "w", encoding='utf8') as f:
        for row in smiles:

            if row.published == None:
                row == str(row)
            elif row.published != None:
                row.published = parse_date(row.published)

            f.write(f'Время настроения: {row.published}' + '\n'
                    + f'🙂: {row.smile_good}' + '\n'
                    + f'🤪: {row.smile_crazy}' + '\n'
                    + f'😑: {row.smile_neutral}' + '\n'
                    + f'😠: {row.smile_agry}' + '\n'
                    + f'😔: {row.smile_sad}' + '\n'
                    + f'_________________________________________'+ '\n')
            
    f.close()



    download_file = os.path.abspath(content_file_name)
    print(download_file)
    
    # download_file = print(f'{os.path.abspath(download_file)}')
    return download_file 






    # smile_good = BooleanField('🙂', default = False,  render_kw={"class": "form-control smile_icon"})
    # smile_crazy = BooleanField('🤪', default = False,  render_kw={"class": "form-control smile_icon"})
    # smile_neutral = BooleanField('😑', default = False,  render_kw={"class": "form-control smile_icon"})
    # smile_angry = BooleanField('😠', default = False,  render_kw={"class": "form-control smile_icon"})
    # smile_sad = BooleanField('😔', default = False,  render_kw={"class": "form-control smile_icon"})