import requests
from bs4 import BeautifulSoup
from time import sleep


def open_url(URL):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
    r = requests.get(URL, headers=headers)
    sleep(2)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def download(url):
    img = requests.get(url, stream=True)
    r = open("путь в папку" + url + "расширение")
    for image in img.iter_content(1024 * 1024):
        r.write(image)
    r.close()


def get_url():
    for count in range(1, 8):
        URL = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        soup = open_url(URL)
        all_cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
        for card in all_cards:
            card_url = "https://scrapingclub.com" + card.find("a").get("href")
            yield card_url


for card_url in get_url():
    page_card_soup = open_url(card_url)
    code_card = page_card_soup.find("div", class_="card mt-4 my-4")
    card_body = page_card_soup.find("div", class_="card-body")
    img_url = "https://scrapingclub.com" + code_card.find("img", class_="card-img-top img-fluid").get("src")
    name = card_body.find("h3", class_="card-title").text.replace("\n", "")
    cost = card_body.find("h4").text
    print(name, "\n", cost, "\n", img_url, "\n\n")