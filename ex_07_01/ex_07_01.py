# Write a program that prompts for a file name,
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below

fname = input("Enter the file name : ")
try :
    fhand = open(fname)
except :
    print("Wrong file name!!!", fname)
    quit()

fdata = fhand.read()
fdata = fdata.rstrip()
print(fdata.upper())    

#Same as the above lines
#for line in fhand :
#    line = line.rstrip()
#    print(line.upper())