import re
import requests
import json

url = 'https://askdjango.github.io/lv3/'
response = requests.get(url)
js_text = response.text

# print(js_text)

matched = re.search(r'var courses = (.*?);', js_text, re.S)
json_string = matched.group(1)

output_list = json.loads(json_string)

for output in output_list:
    print ('{name}{url}'.format(**output))