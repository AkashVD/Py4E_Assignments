# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = "mbox-short.txt" #input()
fhand = open(fname)

hour = []

for line in fhand :
    if line.startswith("From ") :
        word = line.split()
        time = word[5].split(":")
        hour.append(time[0])

count = dict()

for i in hour :
    count[i] = count.get(i,0) + 1

 
for h,v in sorted(count.items()) :
    print(h,v)    


#print(sorted(count.items()))    