from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')


#Retreive all of the anchor tags
tags = soup('tr')
for tag in tags:
	#print(tag.get('href',None))
	print("TAGS ", tag)


