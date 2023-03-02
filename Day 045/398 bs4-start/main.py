from bs4 import BeautifulSoup
#import lxml #truong hop loi


with open('website.html', 'r', encoding="utf-8") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
#loi thi soup = BeautifulSoup(contents, "lxml")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

print(soup.p)

print(soup.find_all(name='a'))

for i in soup.find_all(name='a'):
    print(f'{i.getText()} {i.get("href")}')

print(soup.find(name='h1', id='name'))
print(soup.find(name='h3', class_='heading'))

print(soup.find(selector="p a"))
print(soup.find(selector="#name"))
print(soup.find(selector=".heading"))
