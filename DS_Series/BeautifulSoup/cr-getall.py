from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

#이미 처리한 파일인지 확인하기 위한 변수의 초기화
proc_files = {} 

#HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") #다운받는 문서의 css를 처리하기 위해?
    links += soup.select("a[href]") #href 링크
    result = []
    #href 속성을 추출하고, 링크를 절대 경로로 변환
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href) #기본으로 설정한 url에 링크로 추출한 url합치기
        result.append(url)
    return result

#파일을 다운받고 저장하는 함수
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    
    #이게 뭐지?
    # print('debug : ', o.netloc)
    
    
    if re.search(r"/$", savepath): #폴더라면 index.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    #모두 다운됐는지 확인
    if os.path.exists(savepath):
        return savepath
    #다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=",savedir)
        makedirs(savedir)
    #파일 다운받기
    try:
        print("download=", url)
        urlretrieve(url,savepath)
        time.sleep(1)
        return savepath
    except:
        print("다운실패: ", url)
        return None
    
#html을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return #이미 처리됐다면 실행하지 않음
    proc_files[savepath] = True
    print("anlayze_html", url)
    
    #링크추출
    html = open(savepath, "r", encoding='utf-8').read()
    links = enum_links(html, url)

    for link_url in links:
        #링크가 루트 이외의 경로를 나타낸다면 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        #HTML이라면
        if re.search(r".html$", link_url):
            #재귀적으로 html파일 분석하기
            analyze_html(link_url, root_url)
            continue
        #기타파일
        download_file(link_url)

if __name__ == "__main__":
    #url에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library"
    analyze_html(url, url)
#