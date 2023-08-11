### 네이버 뉴스 헤드라인 크롤링 ###

import requests
from bs4 import BeautifulSoup

URL = 'https://n.news.naver.com/mnews/article/016/0002182307?sid=105'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

headline = soup.select('.media_end_head_headline')
print(headline)