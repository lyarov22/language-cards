import os
from flask import Flask, render_template

from icrawler.builtin import GoogleImageCrawler

from main import get_random_data

app = Flask(__name__, static_url_path='/static')

def search_images(keyword):

    file_path = 'static\\000001.jpg'

    try:
        # Попытка удалить файл
        os.remove(file_path)
        print(f"Файл {file_path} успешно удален.")
    except FileNotFoundError:
        # Обработка исключения, если файл не существует
        print(f"Файл {file_path} не существует. Ничего не удаляется.")
    except Exception as e:
        # Обработка других исключений, если они возникнут
        print(f"Произошла ошибка при удалении файла {file_path}: {e}")
    
    max_num = 1  # Количество изображений, которые вы хотите получить

    # Создаем объект GoogleImageCrawler
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'static'})

    # Настраиваем поиск
    filters = dict(type='photo')  # Можно добавить дополнительные фильтры

    # Запускаем поиск
    results = google_crawler.crawl(keyword=keyword, filters=filters, max_num=max_num, file_idx_offset=0)
    #print(results)

    # Получаем URL первой картинки
    #first_image_url = results[0]['file_url'] if results else None

    # Выводим URL
    #print("URL первой картинки:", first_image_url)
    #return first_image_url
    return 'static\\000001.jpg'



@app.route('/')
def index():

    word = get_random_data()

    search_images(word['Слово или фраза'])

    #img_url = search_images(word['Слово или фраза'])

    image_path = 'static/000001.jpg'

    return render_template('index.html',
        random_word_data = word,
        image_path=image_path
        )

if __name__ == '__main__':
    app.run(debug=True)
