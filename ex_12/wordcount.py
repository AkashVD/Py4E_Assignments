#counting the words from a webpage in the internet
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhand :
	words = line.decode().strip().split()
	for word in words :
		count[word] = count.get(word, 0) + 1

print(count)