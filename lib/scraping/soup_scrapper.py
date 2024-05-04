from requests import get
from bs4 import BeautifulSoup
from typing import Union

class BS4_Web_Scraper:
    def __init__(self) -> None:
        pass

    def get_page(self, url):
        response = get(url)
        return BeautifulSoup(response.content, 'html.parser').prettify()

    def parse_page(self, page):
        pass

def parse_page(url):
    soup = BS4_Web_Scraper()
    page = soup.get_page(url)
    res = parse_page(page)
    return res

if __name__ == '__main__':
    soup = BS4_Web_Scraper()
    url = 'https://www.amazon.com.br/gp/bestsellers/computers/'
    page = soup.get_page(url)