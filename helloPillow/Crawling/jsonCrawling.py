import requests
import json
from bs4 import BeautifulSoup

json_url = 'https://askdjango.github.io/lv2/data.json'
reponse = requests.get(json_url)

json_string = reponse.text

data_list = json.loads(json_string)

for data in data_list:
    # print(data['name'], data['url'])
    print('{name}{url}'.format(**data))