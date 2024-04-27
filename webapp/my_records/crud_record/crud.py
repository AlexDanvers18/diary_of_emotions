from sqlalchemy.sql import func
from webapp.diary_of_emotions.models import TextRecord
from sqlalchemy import desc
from webapp.db import db
from datetime import datetime
from itertools import zip_longest
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
    
    
def get_date_more_then_days(days):
    return datetime.today() - timedelta(days=days)



def complete_text_record(user_id):
    
    # date = get_date_more_then_days(1)
    # texts = db.session.query(TextRecord).filter_by(user_id=1).filter(TextRecord.published > date).all()
    texts = db.session.query(TextRecord).filter_by(user_id=current_user.id).all()
 
    content_file_name = (f'tmp/table_content_{user_id}.txt')

    with open(content_file_name, "w", encoding='utf8') as f:
        for row in texts:

            if row.published == None:
                row == str(row)
            elif row.published != None:
                row.published = parse_date(row.published)

            f.write(f'Время публикации: {row.published}' + '\n'
                    + f'Ситуация: {row.text_situation}' + '\n'
                    + f'Эмоции: {row.text_emotions}' + '\n'
                    + f'Мысли и образы: {row.text_thoughts}' + '\n'
                    + f'Ощущения в теле: {row.text_bodily_sensations}' + '\n'
                    + f'Что думаю о ситуации сейчас: {row.text_result}' + '\n'
                    + f'Победы дня: {row.text_victory}' + '\n'
                    + f'Курьёзы дня: {row.text_curiosity}' + '\n'
                    + f'_________________________________________'+ '\n')
            
    f.close()



    download_file = os.path.abspath(content_file_name)
    print(download_file)

    return download_file 

