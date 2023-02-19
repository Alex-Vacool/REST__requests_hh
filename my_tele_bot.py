# Импорт библиотеки requests для работы с запросами
import requests
# Импорт библиотеки pprint для вывода данных
import pprint
# Импорт библиотеки time
import time
# библиотека для загрузки данных из env
from dotenv import load_dotenv

# метод ищет файл env и переменные из него
load_dotenv()
# достает из файла переменную token
token = getenv('token')


