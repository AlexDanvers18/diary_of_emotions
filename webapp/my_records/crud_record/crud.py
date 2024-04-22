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
    


def complete_text_record(user_id):
    
    texts = db.session.query(TextRecord).filter_by(user_id=1).all()
    # texts = db.session.query(TextRecord).filter_by(current_user.id).all()
 
    content_file_name = (f'tmp/table_content_{user_id}.txt')

    # with open(content_file_name, "w", encoding='cp1251') as f:
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
                    + f'_________________________________________'+ '\n')
            
    f.close()



    download_file = os.path.abspath(content_file_name)
    print(download_file)
    
    # download_file = print(f'{os.path.abspath(download_file)}')
    return download_file 
        # download_file1 = print(f'{os.path.abspath(__file__)}')
        # download_file2 =  f.path

        # return download_file1, download_file2
    #     if row[1] != None:
    #         date = row[1].strftime(f"%d/%B/%Y %H:%M.%f")
    #         date = date
    #     else:
    #         date = "Нет даты"

    #     text_list = []
    #     for cell in row:
    #         date_now = datetime.now().strftime(f"%d/%B/%Y %H:%M.%f")
    #         date_now = date_now
    #         text_list.append(cell)


    #     text_dictionary = dict(zip(text_name_list, text_list))
    #     text_dictionary = {key: text_dictionary.get(key, '') for key in text_name_list}
    #     text_all.append(text_dictionary)


        
    # for text_record in text_all:
    #     for t, v in text_record.items():
    #         t = str(t)
    #         v = str(v)
        
    #         file.write(f'{t}' + f': {v}' + '\n')
    #             # print(f'{t}: {v}')
        
    # file.close()
    # download_file = print(f'{os.path.abspath(__file__)}')
    # return download_file

# if user_id = current_user.id:
#############################3

# def complete_text_record2():
#     texts = db.session.query(TextRecord.published,
#                              TextRecord.text_situation, 
#                              TextRecord.text_emotions, 
#                              TextRecord.text_thoughts, 
#                              TextRecord.text_bodily_sensations, 
#                              TextRecord.text_result)
    
    

 

#     text_all = []
#     text_name_list = ["published", "text_situation", "text_emotions", "text_thoughts", "text_bodily_sensations", "text_result"]
#     number_cell = 0
#     # date_formatted = date.strftime(f"%d/%B/%Y %H:%M")
#     for row in texts:
        
#         if row[0] != None:
#             date = row[0].strftime(f"%d/%B/%Y %H:%M.%f")
#             date = date
#         else:
#             date = "Нет даты"

#         text_list = []
#         for cell in row:
#             date_now = datetime.now().strftime(f"%d/%B/%Y %H:%M.%f")
#             date_now = date_now
#             if date != "Нет даты" and date_now > date:
#                 text_list.append(cell)
#                 # print(f'Дата: {date}. Ячейка называется: {cell}')


#         text_dictionary = dict(zip(text_name_list, text_list))
#         text_dictionary = {key: text_dictionary.get(key, '') for key in text_name_list}
#         text_all.append(text_dictionary)

#     # text_dictionary = dict.fromkeys(text_name_list) | dict(zip(text_name_list, text_list))

#     # print(text_all)
#     for text_record in text_all:
#         for t, v in text_record.items():
#             print(f'{t}: {v}')


###############################3

            # print(f'Дата:{text_record["published"]}')
            # print(f'Ситуация:{text_record["text_situation"]}')
            # print(f'Эмоции:{text_record["text_emotions"]}')
    # print(f'Мыслеобразы:{text_all[0]["text_thoughts"]}')
    # print(f'Ощущения в теле:{text_all[0]["text_bodily_sensations"]}')
    # print(f'Что думаю сейчас:{text_all[0]["text_result"]}')



            # print(f'Айди пользователя: {row.user_id}')
            # print(f'Время публикации: {parse_date(row.published)}')
            # print(f'Ситуация: {row.text_situation}')
            # print(f'Эмоции: {row.text_emotions}')
            # print(f'Мысли и образы: {row.text_thoughts}')
            # print(f'Ощущения в теле: {row.text_bodily_sensations}')
            # print(f'Что думаю о ситуации сейчас: {row.text_result}')
            # print(f'_________________________________________')