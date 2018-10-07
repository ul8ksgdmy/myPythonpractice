import sys
import urllib.request as ur
import urllib.parse as pr

base_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

#sys.argv는 입력받은 내용을 메모리에 저장
#입력받은 내용이 없을 경우 사용법을 출력
if len(sys.argv) <= 1:
    print("Usage: <Region Number>")
    #파이썬을 중단할 때 사용 sys.quit()도 가능
    sys.exit()
#있을 경우 배열의 0번이 아닌 1번 값을 메모리에 저장. 0번 값은 파일 이름
# 예를들어 python .\download-forecast-argv.py 108 이렇게 실행했을 경우
# '.\download-forecast-argv.py'까지가 0번
regionNumber = sys.argv[1]

#매개변수 인코딩 (type of a dict)
values = {
    'stnId' : regionNumber
}

#encode a dict
params = pr.urlencode(values)

#full url
url = base_url + '?' + params

#request & response
res = ur.urlopen(url)

#data
data = res.read()

# sf = 'test3.txt'

# with open(sf, 'w' , encoding='utf-8') as f:
#     f.write(data)

# print('저장되었습니다.')

#바이너리를 문자열로 변환하기
text = data.decode('utf-8')
print(text)