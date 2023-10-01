import requests
from bs4 import BeautifulSoup
from requests import session
from time import sleep
from fake_useragent import UserAgent

def open_URL(url):
    ua = UserAgent()
    headers = {'accept': '*/*', 'user-agent': ua.firefox}
    gfdhjbgdj = 1
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.text, 'lxml')
    card = page.find("main")
    print(card)
    return gfdhjbgdj


url = "https://www.propertyfinder.ae/en/search?c=1&ob=nd&page=1"
open_URL(url)