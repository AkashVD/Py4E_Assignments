# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = "mbox-short.txt"
fhand = open(fname)

count = dict()
for line in fhand :
    if line.startswith("From ") :
        line_lst = line.split()
        count[line_lst[1]] = count.get(line_lst[1], 0) + 1

print(count)

max_count = None
max_key = None

for key,value in count.items() :
    if max_count is None or value > max_count :
        max_count = value
        max_key = key

print(max_key, max_count)        