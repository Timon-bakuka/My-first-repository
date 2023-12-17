import requests
from bs4 import BeautifulSoup


url = 'https://pogoda.mail.ru/prognoz/uralsk/'


r = requests.get(url)
src = r.text

soup =BeautifulSoup(src, 'lxml')

t = soup.find(class_="information__content__temperature")
print("Температура в вашем городе:")
print(t.text)
t = soup.find(class_="information__content__additional__item")
print(t.text)
input()
