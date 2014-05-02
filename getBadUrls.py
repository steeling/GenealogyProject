from bs4 import BeautifulSoup
import urllib2, random


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

f = open("/usr/share/dict/words", "r")
myUrl = "https://www.google.com/search?q="
writeFile = open("badUrls.txt", "w")
urlCounter = 0

text = f.read().split('\n')
text = [a for a in text if len(a) > 5]
while urlCounter < 1000:
	num = int(random.random() * len(text))
	word = text[num]
	del text[num]
	urlCounter += 1
	tempUrl = myUrl + word
	req = urllib2.Request(url=tempUrl,headers=hdr)
	site = urllib2.urlopen(req)
	soup = BeautifulSoup(site.read())
	output = str(soup.find_all('h3', {'class': 'r'})[1].a['href'])
	print urlCounter, output
	writeFile.write(output +'\n')

