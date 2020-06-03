# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_440831.html (Sum ends with 27)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter url :")

html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
tags = soup('span')
for tag in tags:
	
	#print('TAG:', tag)
	#print('URL:', tag.get('href', None))
	#print('Contents:', tag.contents[0])
	#print('Attrs:', tag.attrs)
	sum += int(tag.contents[0])

print("Sum=", sum)