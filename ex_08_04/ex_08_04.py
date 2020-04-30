#  Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#  The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
#  When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")  #"romeo.txt"
try:
    fhand = open(fname)
except:
    print("Wrong File Name!!!", fname)

new_lst = list()
for line in fhand :
    line_lst = line.split()
    for i in line_lst :
        if i not in new_lst:
            new_lst.append(i)

new_lst.sort()        
print(new_lst) 