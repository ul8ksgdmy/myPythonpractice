from bs4 import BeautifulSoup
soup = BeautifulSoup("<p><a href='a.html'>test</a></p>", "html.parser")
soup.prettify()
# '<p>\n <a href="a.html">\n  test\n </a>\n</p>'
a = soup.p.a
type(a.attrs)
# <class 'dict'>
'href' in a.attrs
# True
a['href']
# 'a.html'