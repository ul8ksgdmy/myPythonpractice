#영진닷컴에서 프로그래밍의 인기도 순으로 책 제목 뽑기
#params = child_cate_cd=9&orderByCd=2

import requests
import time
from bs4 import BeautifulSoup

url = "http://www.youngjin.com/book/book_list.asp"
#파라미터
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

cate_cd = '1'
child_cate_cd = '9'
orderByCd = '2'
goPage = '1'

params = {'cate_cd': cate_cd, 'child_cate_cd':child_cate_cd, 'orderByCd':orderByCd, 'goPage':goPage}
res = requests.get(url, headers=headers, params=params)
res.encoding = None #인코딩 추측을 할 수 없도록 미리 지정.
html = BeautifulSoup(res.text, 'lxml')

totalpages = html.select('p.paging a')
print(len(totalpages))
lp = int(len(totalpages)+1)

for i in range(1, lp):
    params = {'child_cate_cd':child_cate_cd, 'orderByCd':orderByCd, 'goPage':i}
    res = requests.get(url, headers=headers, params=params)
    res.encoding = None #인코딩 추측을 할 수 없도록 미리 지정.
    html = BeautifulSoup(res.text, 'lxml')

    for a in html.select('li a span.title'):
        print(a.text.strip())
    time.sleep(1)
    