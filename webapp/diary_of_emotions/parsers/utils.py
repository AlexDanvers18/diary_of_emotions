import requests

from webapp.db import db
from webapp.diary_of_emotions.models import Articles

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
    
    

def save_articles(title, url, published):
    articles_exists = Articles.query.filter(Articles.url == url).count()
    if not articles_exists:
        new_articles = Articles(title=title, url=url, published=published)
        db.session.add(new_articles)
        db.session.commit()




