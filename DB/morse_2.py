#모스부호를 스크랩해서 파일로 저장하고 모스부호를 계산한다.

#modules and classes to use
import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import re

#webpage
# url = 'https://librewiki.net/wiki/%EB%AA%A8%EC%8A%A4_%EB%B6%80%ED%98%B8' #주소1
url = 'http://codingdojang.com/scode/469?langby=python#answer-filter-area' #주소2
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
res = requests.get(url, headers=headers)
# print(res)

#info
data = res.text
# print(data)

#parsing
soup = BeautifulSoup(data, 'lxml')
# print(soup.text)

# storage to save signals
signals = []

# collect text data
# for t in soup.select('.wikitable tr td'): #주소1
for t in soup.select('div.markdown_area.answer-content > table > tbody tr td'): #주소2
    pattern = re.compile(r'\s+')
    t_data = re.sub(pattern,'', t.text)
    print(t_data)
    # print(t.text.strip())
    signals.append(t_data)

# #string data into a Dictionary list
allData = OrderedDict()
# for i in range(int(len(soup.select('.wikitable tr td'))/2)): #주소1
for i in range(int(len(soup.select('div.markdown_area.answer-content > table tr td'))/2)): #주소2
    #dictionary 형태로 저장.
    allData[signals[2*i+1]] = signals[2*i]
    # allData[signals[2*i]] = signals[2*i+1]
    # print(signals[2*i] + ' ' +signals[2*i+1])

#save file
with open('morse.json', 'w', encoding='utf-8') as f:
    json.dump(allData, f, ensure_ascii=False, sort_keys=True, indent=4)


wordslists = []

#데이터 분석
morse = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
# 빈 칸이 1칸일 경우 구분자로 인식되지만 2칸일 경우 ''의 형태로 저장된다.
wordslists = morse.split(" ")

result = ""
for wordlist in wordslists:
    if wordlist == '':
        result += ' '
    else:
        result += allData[wordlist]
print(result)
