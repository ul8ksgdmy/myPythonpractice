import urllib.request as ur
from bs4 import BeautifulSoup as bs

#get response
url = 'https://finance.naver.com/marketindex/'
res = ur.urlopen(url)

#parsing
soup = bs(res, 'html.parser')

#현재는 의미있는 문자열이기 때문에 다시 의미없는 string으로 바꿔야 한다.
#show me
for price in soup.select('a.head.usd div span.value'):
    print(price.string)

