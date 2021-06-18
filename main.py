import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get('https://habr.com/ru/all/')

if not response.ok:
    raise ValueError('Responce not valid')

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:

    news_text = article.find('div', class_='post__text')
    news_words = set(re.split('[\s\W]+', news_text.text))
    if KEYWORDS & news_words:
        post_time = article.find('span', class_='post__time').text
        post_header = article.find('a', class_='post__title_link')
        print(f'{post_time} - {post_header.text} - {post_header.attrs.get("href")} ')


