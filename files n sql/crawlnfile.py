#모스부호를 스크랩해서 파일로 저장하고 모스부호를 계산한다.
#리브레 위키에서 모스부호를 가져옴.
#https://librewiki.net/wiki/%EB%AA%A8%EC%8A%A4_%EB%B6%80%ED%98%B8
#mw-content-text > table:nth-child(10) > tbody > tr:nth-child(2) > td:nth-child(1)



#modules and classes to use
import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import re

#webpage
url = 'https://librewiki.net/wiki/%EB%AA%A8%EC%8A%A4_%EB%B6%80%ED%98%B8'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
res = requests.get(url, headers=headers)
print(res)

#info
data = res.text
print(data)

#parsing
soup = BeautifulSoup(data, 'lxml')

print(soup.text)

# storage to save signals
# alphabets = []
signals = []

for t in soup.select('.wikitable tr td'):
    pattern = re.compile(r'\s+')
    t_data = re.sub(pattern,'', t.text)
    print(t_data)
    # print(t.text.strip())
    signals.append(t_data) #분명 encode문제 발생할 것으로 보임

# #change file
allData = OrderedDict()
for i in range(int(len(soup.select('.wikitable tr td'))/2)):
    allData[signals[2*i]] = signals[2*i+1]
    # print(signals[2*i] + ' ' +signals[2*i+1])

# #save file
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(allData, f, ensure_ascii=False, indent=4)