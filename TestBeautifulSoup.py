#import urllib
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#req=urlopen("http://www.imooc.com/")
#bsObj=BeautifulSoup(req.read(),'html.parser')
#print(bsObj.title)

##############################################
#抓获异常
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html=urlopen(url)
	except (HTTPError,URLError) as e:
		return None
	try:
		bsObj=BeautifulSoup(html.read(),'html.parser')
		title=bsObj.title
	except AttributeError as e:
		return None
	return title

title = getTitle('http://www.sdfskk.com/')
if title == None:
	print('Title could  not be found')
else:
	print(title)

##############################################
#使用request
#import urllib 
#import urllib.request

#req=urllib.request.urlopen('http://www.imooc.com/')
#buf=req.read()
#print(buf)

