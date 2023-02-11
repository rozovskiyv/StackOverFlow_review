import requests
import json
import datetime
from pprint import pprint

# Формирование запроса
url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'fromdate': int((datetime.datetime.now() - datetime.timedelta(days=2)).timestamp()),
    'todate': int(datetime.datetime.now().timestamp()),
    'tagged': 'python',
    'site': 'stackoverflow',
}
response = requests.get(url, params=params)

# Обработка ответа

data = json.loads(response.text)
questions = data['items']
for question in questions:
    print(question['title'])
