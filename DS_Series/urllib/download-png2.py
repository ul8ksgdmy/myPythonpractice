import urllib.request as ur

url = 'http://uta.pw/shodou/img/28/214.png'
sf = 'test2.png'

# 메모리에 저장한다.
mem = ur.urlopen(url).read()

# with open을 이용하여 파일로 저장한다.
#'wb'는 write with binary
with open(sf, mode='wb') as f:
    f.write(mem)

print('저장되었습니다.')
