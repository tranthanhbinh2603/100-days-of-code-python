#https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get('https://news.ycombinator.com/').text, "html.parser")

list = []
for i in soup.find_all("span", {"class": "subline"}):
    list_2 = []
    z = i.find("span", {"class": "score"})
    list_2.append(z.string)
    list.append(list_2)
list.append([])

idx = 0
for i in soup.find_all("span", {"class": "titleline"}):
    list[idx].append(i.find_all("a")[0].string)
    list[idx].append(i.find_all("a")[0]['href'])
    idx+=1

for i in list:
    print(i)
