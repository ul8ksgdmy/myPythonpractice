import sys
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib.parse as up

base_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

#query를 이용해 조회가 가능한 프로그램. 매개변수를 이용함.

#예외처리
if len(sys.argv) <= 1 :
    print('rewrite')
regionNumber = sys.argv[1]

#dict
values = {
    'stnId' : regionNumber
}

#encode a dict
params = up.urlencode(values)

#full url
full_url = base_url + '?' + params

#response
res = ur.urlopen(full_url)

#분석
soup = bs(res,'html.parser')

d_title = soup.find('title').string
#find를 이용했기 때문에 가장 먼저 나온 wf 하나만 찾는다.
d_wf = soup.find('wf').string

print(d_title)
print(d_wf)