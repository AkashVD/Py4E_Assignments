# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter the file name : ")
try:
    fhand = open(fname) #mbox-short.txt
except:
    print("Wrong file name!!!", fname)

count = 0
total = 0
for line in fhand :
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count += 1
    val_ind = line.find(":")
    value = float(line[val_ind+1:])
    total += value

print("Average spam Confidence:", total/count)
