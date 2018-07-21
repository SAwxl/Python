from bs4 import BeautifulSoup
import urllib

url = "http://movie.douban.com/review/best/?start="
html = urllib.urlopen(url)
#data = html.read()
#fhandle = open("douban.txt","wb")
#fhandle.write(data)

soup = BeautifulSoup(html, "lxml")
data = soup.prettify()
print(type(data))
data = data.encode("utf-8")
print(type(data))
fhandle = open("webpage_content.txt","wb")
fhandle.write(data)