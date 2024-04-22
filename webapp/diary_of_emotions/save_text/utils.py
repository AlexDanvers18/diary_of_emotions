import requests

from webapp.db import db
from webapp.diary_of_emotions.models import TextRecord

def get_html(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
    }
    try:
        url = url.strip()
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError) as e:
        print(e)
        print('Сетевая ошибка')
        return False
    
    

def save_text_record(user_id, name, title, published, text_record):
    new_text_record = TextRecord(id=user_id, name=name, title=title, published=published, text=text_record)
    db.session.add(new_text_record)
    db.session.commit()




