from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set() #중복방지
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal links found on a page after parsing
def getInternalLinks(bsObj, includeUrl):
    #http + :// + 주소 - 이유는 알 수 없지만 주소를 분리해서 다시 접합해야 하는 이유가 있었을 듯.
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #내부링크의 조건은 /로 시작하거나 현재 주소를 가질 것.
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
            
#Retrieves a list of all external links found on a page after parsing
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #외부링크의 조건은 http 혹은 www로 시작하고 현재 주소를 가지지 않을 것
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

#링크 뽑기
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    # 현재 페이지에서 외부링크로 수집한 링크를 가져온다.
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    # 수집한 링크가 하나도 없을 경우
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        # 내부링크를 가져와서
        internalLinks = getInternalLinks(bsObj, domain)
        # 아무것이나 하나 내부링크를 내보낸다.
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    # 수집한 링크가 있을 경우
    else:
        #외부링크 중 아무것이나 하나를 꼽아 내보낸다.
        return externalLinks[random.randint(0, len(externalLinks)-1)]

#재귀 함수를 만들기 위한 실행 함수
def followExternalOnly(startingSite):
    #내부 혹은 외부링크를 가져와서
    externalLink = getRandomExternalLink(startingSite)
    #출력하고
    print("Random link is: "+externalLink)
    #다시 실행
    followExternalOnly(externalLink)
            
#Collects a list of all external URLs found on the site
# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
#     html = urlopen(siteUrl)
#     domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
#     bsObj = BeautifulSoup(html, "html.parser")
#     internalLinks = getInternalLinks(bsObj,domain)
#     externalLinks = getExternalLinks(bsObj,domain)

#     for link in externalLinks:
#         if link not in allExtLinks:
#             allExtLinks.add(link)
#             print(link)
#     for link in internalLinks:
#         if link not in allIntLinks:
#             allIntLinks.add(link)
#             getAllExternalLinks(link)

followExternalOnly("http://www.naver.com")

# allIntLinks.add("http://oreilly.com")
# getAllExternalLinks("http://oreilly.com")