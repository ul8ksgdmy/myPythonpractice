#크롤링 할 대상은 HTML문서 + JSON
#이미지 (이번 포스트에서 다룰 파트)
#PDF, EXCEL등 여러가지 정적 파일

#jpg: 주로 이미지 저장할 때 이미지 품질 옵션이 있으며 0~100 까지 있음
#gif: 움직이는 이미지. 저품질 (저품질인 이유는 gif에서 지원하는 팔레트가 적기 때문에)
#png: 투명지원되는 이미지 포맷

#목차
# 1. 이미지 다운받기
# 2. 고화질 이미지를 다운받더라도, 경우에 따라 작은 용량으로 줄일 필요가 있음 -> 이것을 썸네일 처리라고 함
# 3. 대개 여러개의 파일로 나뉘어져있음 -> 이럴경우 이미지 합치기
# Ex) 웹툰 (웹툰의 이미지가 하나의 파일일 경우, 로딩에 긴 시간이 필요하므로 나뉘어서 올려짐)
# 4. 이미지를 다른 포맷으로 변환하기(jpg, png 등)


# 1. 이미지다운

import os
from PIL import Image
import requests
#이미지 확인
# from IPython.display import Image


image_url = ('https://ee5817f8e2e9a2e34042-3365e7f0719651e5b8d0979bce83c558.ssl.cf5.rackcdn.com/python.png')

# image = requests.get(image_url).content #image원본의 인스턴스화
# filename = os.path.basename(image_url) #image_url에서 가장 마지막의 파일명만 획득
# with open(filename, 'wb') as f: #쓰기, 바이너리 (왜?)
#     f.write(image) #파일저장

# Image(filename='python.png') #이미지 확인 (주피터 노트북을 써야 보이는 듯?)

# 2. 이미지 품질 낮추기

