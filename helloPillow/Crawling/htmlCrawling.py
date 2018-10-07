import requests
from bs4 import BeautifulSoup

html_url = 'https://askdjango.github.io/lv1/'
response = requests.get(html_url)

# print(response) #200응답
# print(response.text) #pharsed 되기 전의 tag들이 출력


html = response.text
bstext = BeautifulSoup(html, 'lxml')

#bs은 xpath를 지원하지 않는다.
for ctext in bstext.select('li.course') :
    print(ctext.text)
