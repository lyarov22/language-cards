import random
import openpyxl

# Укажите путь к вашему файлу Excel
excel_file_path = "./8k.xlsx"

# Открываем файл
workbook = openpyxl.load_workbook(excel_file_path)

# Выбираем активный лист
sheet = workbook.active

# Создаем список для хранения данных
data = []

# Проходим по строкам в листе Excel
for row in sheet.iter_rows(min_row=2, values_only=True):  # Начинаем с второй строки, предполагая, что первая строка - заголовок
    word = row[1]
    transcription = row[2]
    translation = row[3]

    # Добавляем данные в список
    data.append({"Слово или фраза": word, "Транскрипция": transcription, "Перевод": translation})

# # Выводим полученные данные
# for item in data:
#     print(item)

def get_random_data():
    random_word_data = random.choice(data)
    return random_word_data
