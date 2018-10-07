import urllib.request as ur
import urllib.parse as pr

base_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

#매개변수 인코딩 (type of a dict)
values = {
    'stnId' : '108'
}

#encode a dict
param = pr.urlencode(values)

#full url
url = base_url + '?' + param

rs = ur.urlopen(url)
data = rs.read()
sf = 'test3.txt'

with open(sf, 'w' , encoding='utf-8') as f:
    f.write(data)

print('저장되었습니다.')









#response
res = ur.urlopen(url)

#data
data = res.read()

#바이너리를 문자열로 변환하기
text = data.decode('utf-8')
print(text)