#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

fname = input("Enter the file name :")#"regex_sum_42.txt"

fhand = open(fname)

sum = 0

for line in fhand :
	if len(re.findall('[0-9]+',line)) >= 1 :
		num = re.findall('[0-9]+', line)
		for i in num :
			sum += int(i)
		#print(num)

print(sum)		