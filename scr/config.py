import requests
from bs4 import BeautifulSoup as b
import random

URL = 'https://anekdotov.net/sms/'
URL_C = 'https://citatnica.ru/citaty/tsitaty-velikih-filosofov-210-tsitat'
def parser_1(url):
    r = requests.get(url)
# print(r.status_code)
    soup = b(r.text, 'html.parser')
    anek = soup.find_all('div', class_='anekdot')
    return [c.text for c in anek]
list_anek = parser_1(URL)
random.shuffle(list_anek)

def parser_2(url):
    r = requests.get(url)
# print(r.status_code)
    soup = b(r.text, 'html.parser')
    citata = soup.find_all('div', class_='su-note-inner su-u-clearfix su-u-trim')
    return [c.text for c in citata]
list_citati = parser_2(URL_C)
random.shuffle(list_citati)
