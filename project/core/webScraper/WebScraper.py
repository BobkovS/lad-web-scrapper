from datetime import datetime
from http import HTTPStatus
from time import sleep

import requests
from bs4 import BeautifulSoup

from project.core.dbLayer import scraping_obj
from project.core.domain import Product
from project.utils.utils import ignore_errors_wrapper


class WebScraper:
    def __init__(self):
        self.web_page_url = "https://www.toledo24.pro/catalog/ustanovka-vyklyuchateli-rozetki-i-aksessuary/"

    def parse_web_page(self):
        web_page_response = requests.get(self.web_page_url)

        if not web_page_response.status_code == HTTPStatus.OK:
            raise Exception(f"Запрос к веб-странице завершился с ошибкой: {web_page_response.reason}")

        web_page_html = BeautifulSoup(web_page_response.content.decode(), 'html.parser')
        web_page_product_list = web_page_html.find_all("div", {"class": "product-card js-product-item"})

        scraping_datetime = datetime.now()
        scraping_obj.push(scraping_datetime)

        for web_page_product in web_page_product_list:
            Product(self.extract_product_title(web_page_product), self.extract_product_amount(
                web_page_product), self.extract_product_price(web_page_product)).save(scraping_datetime)

    @staticmethod
    def extract_product_title(web_page_product):
        search_result = web_page_product.find("a", {"class": "link product-name"}, {"itemprop": "name"})
        return search_result.text.strip() if search_result is not None else ""

    @staticmethod
    def extract_product_amount(web_page_product):
        search_result = web_page_product.find("div", {"class": "amount-title"})
        return search_result.text.strip().split()[0] if search_result is not None else 0

    @staticmethod
    def extract_product_price(web_page_product):
        search_result = web_page_product.find("div", {"class": "price"})
        return search_result.text.strip().split()[0] if search_result.text.strip() != "" else None

    def run_scraper(self):
        while True:
            with ignore_errors_wrapper():
                self.parse_web_page()
            sleep(60)
