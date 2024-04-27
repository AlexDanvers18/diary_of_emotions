from sqlalchemy.sql import func
from webapp.diary_of_emotions.models import SmileRecord, EmoRecord
from webapp.diary_of_emotions.forms import EmotionForm, BooleanField
from sqlalchemy import desc
from webapp.db import db
from datetime import datetime
from flask_login import current_user
# from db import db_session
from datetime import datetime, timedelta


import locale
import platform






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
    



content_file_name = (f'tmp/smile_content.txt')


def get_date_more_then_days(days):
    return datetime.today() - timedelta(days=days)


def complete_smile_record(user_id):

    date = get_date_more_then_days(7)
    smiles = db.session.query(SmileRecord).filter_by(user_id=current_user.id).filter(SmileRecord.published > date).all()

    # content_file_name = (f'tmp/smile_content_{user_id}.txt')

    smile_dict = {}

    smile_list_good = []
    smile_list_crazy = []
    smile_list_neutral = []
    smile_list_agry = []
    smile_list_sad = []

 
    
    for row in smiles:

        smile_list_good.append(int(row.smile_good))
        smile_list_crazy.append(int(row.smile_crazy))
        smile_list_neutral.append(int(row.smile_neutral))
        smile_list_agry.append(int(row.smile_agry))
        smile_list_sad.append(int(row.smile_sad))


        smile_list = ["🙂", "🤪", "😑", "😠", "😔"]
        sum_good = [sum(smile_list_good), sum(smile_list_crazy), sum(smile_list_neutral), sum(smile_list_agry), sum(smile_list_sad)]
        smile_dict = dict(zip(smile_list, sum_good))



    # with open(content_file_name, "w", encoding='utf8') as f:

    #     for k, v in smile_dict.items():
    #         f.write(k * v + '\n')

    # f.close()

    return smile_dict
        


def complete_emo_record(user_id):

    date = get_date_more_then_days(7)
    emotions = db.session.query(EmoRecord).filter_by(user_id=current_user.id).filter(EmoRecord.published > date).all()
    # emotions = db.session.query(EmoRecord).filter_by(user_id=current_user.id).filter(EmoRecord.published > date).all()



    emo_list_1 = []
    emo_list_2 = []
    emo_list_3 = []
    emo_list_4 = []
    emo_list_5 = []
    emo_list_6 = []
    emo_list_7 = []
    emo_list_8 = []
    emo_list_9 = []
    emo_list_10 = []
    emo_list_11 = []
    emo_list_12 = []
    emo_list_13 = []
    emo_list_14 = []
    emo_list_15 = []
    emo_list_16 = []
    emo_list_17 = []
    emo_list_18 = []
    emo_list_19 = []
    emo_list_20 = []
    emo_list_21 = []
    emo_list_22 = []
    emo_list_23 = []
    emo_list_24 = []
    emo_list_25 = []
    emo_list_26 = []
    emo_list_27 = []
    emo_list_28 = []
    emo_list_29 = []
    emo_list_30 = []
    emo_list_31 = []
    emo_list_32 = []
    emo_list_33 = []
    emo_list_34 = []
    emo_list_35 = []
    emo_list_36 = []
    emo_list_37 = []
    emo_list_38 = []
    emo_list_39 = []
    emo_list_40 = []
    emo_list_41 = []
    emo_list_42 = []
    emo_list_43 = []
    emo_list_44 = []
    emo_list_45 = []


    # emo_file_name = (f'tmp/emo_content_{user_id}.txt')


    for row in emotions:
        emo_list_1.append(int(row.emotion_1))
        emo_list_2.append(int(row.emotion_2))
        emo_list_3.append(int(row.emotion_3))
        emo_list_4.append(int(row.emotion_4))
        emo_list_5.append(int(row.emotion_5))
        emo_list_6.append(int(row.emotion_6))
        emo_list_7.append(int(row.emotion_7))
        emo_list_8.append(int(row.emotion_8))
        emo_list_9.append(int(row.emotion_9))
        emo_list_10.append(int(row.emotion_10))
        emo_list_11.append(int(row.emotion_11))
        emo_list_12.append(int(row.emotion_12))
        emo_list_13.append(int(row.emotion_13))
        emo_list_14.append(int(row.emotion_14))
        emo_list_15.append(int(row.emotion_15))
        emo_list_16.append(int(row.emotion_16))
        emo_list_17.append(int(row.emotion_17))
        emo_list_18.append(int(row.emotion_18))
        emo_list_19.append(int(row.emotion_19))
        emo_list_20.append(int(row.emotion_20))
        emo_list_21.append(int(row.emotion_21))
        emo_list_22.append(int(row.emotion_22))
        emo_list_23.append(int(row.emotion_23))
        emo_list_24.append(int(row.emotion_24))
        emo_list_25.append(int(row.emotion_25))
        emo_list_26.append(int(row.emotion_26))
        emo_list_27.append(int(row.emotion_27))
        emo_list_28.append(int(row.emotion_28))
        emo_list_29.append(int(row.emotion_29))
        emo_list_30.append(int(row.emotion_30))
        emo_list_31.append(int(row.emotion_31))
        emo_list_32.append(int(row.emotion_32))
        emo_list_33.append(int(row.emotion_33))
        emo_list_34.append(int(row.emotion_34))
        emo_list_35.append(int(row.emotion_35))
        emo_list_36.append(int(row.emotion_36))
        emo_list_37.append(int(row.emotion_37))
        emo_list_38.append(int(row.emotion_38))
        emo_list_39.append(int(row.emotion_39))
        emo_list_40.append(int(row.emotion_40))
        emo_list_41.append(int(row.emotion_41))
        emo_list_42.append(int(row.emotion_42))
        emo_list_43.append(int(row.emotion_43))
        emo_list_44.append(int(row.emotion_44))
        emo_list_45.append(int(row.emotion_45))

 
        
        sum_list_1 = sum(emo_list_1)
        sum_list_2 = sum(emo_list_2)
        sum_list_3 = sum(emo_list_3)
        sum_list_4 = sum(emo_list_4)
        sum_list_5 = sum(emo_list_5)
        sum_list_6 = sum(emo_list_6)
        sum_list_7 = sum(emo_list_7)
        sum_list_8 = sum(emo_list_8)
        sum_list_9 = sum(emo_list_9)
        sum_list_10 = sum(emo_list_10)
        sum_list_11 = sum(emo_list_11)
        sum_list_12 = sum(emo_list_12)
        sum_list_13 = sum(emo_list_13)
        sum_list_14 = sum(emo_list_14)
        sum_list_15 = sum(emo_list_15)
        sum_list_16 = sum(emo_list_16)
        sum_list_17 = sum(emo_list_17)
        sum_list_18 = sum(emo_list_18)
        sum_list_19 = sum(emo_list_19)
        sum_list_20 = sum(emo_list_20)
        sum_list_21 = sum(emo_list_21)
        sum_list_22 = sum(emo_list_22)
        sum_list_23 = sum(emo_list_23)
        sum_list_24 = sum(emo_list_24)
        sum_list_25 = sum(emo_list_25)
        sum_list_26 = sum(emo_list_26)
        sum_list_27 = sum(emo_list_27)
        sum_list_28 = sum(emo_list_28)
        sum_list_29 = sum(emo_list_29)
        sum_list_30 = sum(emo_list_30)
        sum_list_31 = sum(emo_list_31)
        sum_list_32 = sum(emo_list_32)
        sum_list_33 = sum(emo_list_33)
        sum_list_34 = sum(emo_list_34)
        sum_list_35 = sum(emo_list_35)
        sum_list_36 = sum(emo_list_36)
        sum_list_37 = sum(emo_list_37)
        sum_list_38 = sum(emo_list_38)
        sum_list_39 = sum(emo_list_39)
        sum_list_40 = sum(emo_list_40)
        sum_list_41 = sum(emo_list_41)
        sum_list_42 = sum(emo_list_42)
        sum_list_43 = sum(emo_list_43)
        sum_list_44 = sum(emo_list_44)
        sum_list_45 = sum(emo_list_45)



        
    emotion_name_list = ["Радость", "Грусть", "Тревога", "Любопытство","Злость", "Умиротворение", "Интерес", "Сомнение", "Вина", "Стыд", "Доверие",
                         "Спокойствие", "Благодарность", "Лень", "Жалость", "Отчаяние", "Печаль", "Восторг", "Освобождение", "Ревность", "Зависть", "Обида", "Возмущение", 
                          "Досада", "Принятие", "Ненависть", "Ожидание", "Ярость", "Негодование", "Недовольство", "Изумление", "Забота", "Нежность",
                          "Загнанность", "Скука", "Тоска", "Безысходность", "Скорбь", "Оцепенение", "Ужас", "Сочувствие", "Гордость", "Влюбленность", 
                          "Безопасность", "Блаженство"]
    
    sum_emo = [sum_list_1, sum_list_2, sum_list_3, sum_list_4, sum_list_5, sum_list_6, sum_list_7, sum_list_8, sum_list_9, sum_list_10,
                sum_list_11, sum_list_12, sum_list_13, sum_list_14, sum_list_15, sum_list_16, sum_list_17, sum_list_18, sum_list_19, sum_list_20,
                sum_list_21, sum_list_22, sum_list_23, sum_list_24, sum_list_25, sum_list_26, sum_list_27, sum_list_28, sum_list_29, sum_list_30,
                sum_list_31, sum_list_32, sum_list_33, sum_list_34, sum_list_35, sum_list_36, sum_list_37, sum_list_38, sum_list_39, sum_list_40,
                sum_list_41, sum_list_42, sum_list_43, sum_list_44, sum_list_45
                ]
    emo_dict = dict(zip(emotion_name_list, sum_emo))
    


    # for k, v in emo_dict.items():
    #     if v >= 5: 
    #         print(f'Частая эмоция на этой неделе: {k}. Её ты испытывал(-а) {v} раз.')



    # with open(emo_file_name, "w", encoding='utf8') as f:

    #     for k in max_emo_list:
    #         f.write(f'Чаще всего за последнее время ты испытывал(-а): {k}' + '\n')

    # f.close()

    return emo_dict