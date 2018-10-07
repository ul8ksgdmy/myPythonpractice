import urllib.request as ur

url = 'http://uta.pw/shodou/img/28/214.png'
sf = 'test.png'

# 메모리에 저장하지 않고 바로 저장한다.
ur.urlretrieve(url,sf)
print('저장되었습니다.')

