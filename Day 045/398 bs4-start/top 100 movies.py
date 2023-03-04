#https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
from bs4 import BeautifulSoup
import requests

content = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
soup = BeautifulSoup(content, 'html.parser')

list = soup.find_all("h3", {'class': 'title'})
list.reverse()
with open('output.txt', 'w', encoding='utf-8') as f:
    for i in list:
        f.write(f'{i.string}\n')