import requests
from bs4 import BeautifulSoup
from requests import session
from time import sleep
from fake_useragent import UserAgent

def give_inform():
    ua = UserAgent()
    headers = {'accept': '*/*', 'user-agent': ua.firefox}
    count = 1
    url = "https://www.propertyfinder.ae/en/search?c=1&ob=nd&page=1"
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.text, 'lxml')
    card = page.find("main")
    print(card)

give_inform()