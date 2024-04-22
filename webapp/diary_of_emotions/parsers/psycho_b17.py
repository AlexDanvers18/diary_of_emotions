from datetime import datetime, timedelta
import locale
import platform
from bs4 import BeautifulSoup
from urllib.request import urlopen


from webapp.db import db
from webapp.diary_of_emotions.models import Articles
from webapp.diary_of_emotions.parsers.utils import get_html, save_articles


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str.split('.')[0], '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()
    

def get_articles_snippets():
    html = get_html("https://www.b17.ru/article/?tag=%DD%EC%EE%F6%E8%FF")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_articles = soup.find('div', class_='art_list_all').findAll('div', class_='art_list2')
        for article in all_articles:
            title = article.find('span', class_='h2').text
            url = article.find('a', class_='h')['href']
            published = article.find('div', class_='icons_view_n').text
            # published = parse_habr_date(published)
            save_articles(title, url, published)





# def get_articles_content():
#     article_html_code = str(urlopen('https://www.b17.ru/article/329086/').read(),'windows-1251')
#     soup = BeautifulSoup(article_html_code, "html.parser")
#     soup = soup.find('div', {"class": 'maket_white_box_top'}).decode_contents()
#     print(soup)





# def get_articles_content():
#     # article_without_text = Articles.query.filter(Articles.text.is_(None))
#     article_list = Articles.query.order_by(Articles.title.desc()).all()
#     for one_article in article_list:
#         html = get_html(one_article.url)
#         if html:
#             one_article = BeautifulSoup(html, 'html.parser')
#             one_article = one_article.find('div', class_='maket_white_box_top').decode_contents()
#             if one_article:
#                 one_article.text = one_article
#                 db.session.add(one_article)
#                 db.session.commit()

        # url_list.append(el.find("a", class_="h")["href"])


table_list = []
content_file_name = 'table_content.txt'

def get_my_records():
    html = get_html("http://localhost:5000/my_records/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_records = soup.find('div', class_='col-12').findAll('table', class_='table-feel')
        table_list.append(all_records)
        

    file = open(content_file_name, "w")
    for x in table_list:
        file.write(x + '\n')
        
    file.close()





url_list = []
content_file_name = 'url_content.txt'

def get_articles_content():
    html = get_html("https://www.b17.ru/article/?tag=%DD%EC%EE%F6%E8%FF")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_articles = soup.find('div', class_='art_list_all').findAll('div', class_='art_list2')
        for article in all_articles:
            url = article.find('a', class_='h')['href']
            url_list.append(url)
        

    file = open(content_file_name, "w")
    for x in url_list:
        file.write('https://www.b17.ru' + x + '\n')
        
    file.close()




def get_one_article_text():
    
    with open(content_file_name) as file_1:
        lines = file_1.readlines()
    file_1.close

    content_text_file_name = 'text_content.txt'
    f = open(content_text_file_name, "w")

    for line in lines:
        html = get_html(line)
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find('div', {"class": 'maket_white_box_top'}).decode_contents()



        # получаем исходный код страницы
        inner_html_code = str(urlopen(line).read(),'windows-1251')
        inner_soup = BeautifulSoup(inner_html_code, "html.parser")
        inner_soup = inner_soup.find('div', {"class": 'maket_white_box_top'}).decode_contents()
        

        f.write(soup)

    f.close()
        
    



# def get_articles_content():
#     # считываем страницу со всеми адресами
#     html_code = str(urlopen('https://www.b17.ru/article/?tag=%DD%EC%EE%F6%E8%FF').read(),'windows-1251')
#     soup = BeautifulSoup(html_code, 'html.parser')
#     s = soup.find('div', class_='art_list_all')
 

#      # тут будут все найденные адреса
#     url_list = []
#     for el in s.select("div:has(a)"): 
#         if el is None:
#             el = 0
#         else:
#             print(el.find("a", {"class": 'h'})["href"])
#             url_list.append(el.find("a", {"class": 'h'})["href"])

    

#     # имя файла для содержимого каждой рубрики

         