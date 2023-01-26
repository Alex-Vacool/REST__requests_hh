from pprint import pprint
from requests import get
from json import dump as jdump

url = 'https://api.hh.ru/vacancies'
params = {'text': 'python'}
res = get(url, params=params).json()
print(res['found'])
pprint(res['items'])

# сохранение файла с результами работы
with open('res.json', mode='w') as f:
    jdump([res], f)

