import json
from bs4 import BeautifulSoup
from icrawler import Parser
import requests

class GoogleParser(Parser):

    def parse(self, response):
        soup = BeautifulSoup(response.content, 'lxml')
        image_divs = soup.find_all('div', class_='rg_di rg_el ivg-i')
        for div in image_divs:
            meta = json.loads(div.text)
            if 'ou' in meta:
                yield dict(file_url=meta['ou'])

# Создайте экземпляр GoogleParser
google_parser = GoogleParser()

# Вызовите метод parse для обработки данных
results = list(google_parser.parse('cat'))

# Выведите результат в консоль
for result in results:
    print(result)
