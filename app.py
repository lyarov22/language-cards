from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests

from main import random_word_data

app = Flask(__name__)

def get_image_url(word):
    # Формируем URL для запроса на freepik
    search_url = f"https://ru.freepik.com/search?format=search&last_filter=query&last_value={word}&query={word}"

    # Отправляем запрос на страницу freepik
    response = requests.get(search_url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем первую картинку на странице
        img_tag = soup.find('img', class_='landscape loaded')

        if img_tag:
            # Получаем URL изображения
            img_url = img_tag['src']
            return img_url
    return None

@app.route('/')
def index():
    greeting_message = 'Привет, мир! Это мой простой веб-сервер на Flask.'

    word = random_word_data

    img_url = get_image_url(word)

    return render_template('index.html',
        greeting=greeting_message,
        random_word_data = random_word_data,
        img_url = img_url
        )

if __name__ == '__main__':
    app.run(debug=True)
