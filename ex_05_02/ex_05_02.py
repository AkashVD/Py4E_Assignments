#Finding largest and smallest along with error checking of inputs

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        fnum = float(num)
    except :
        print("Invalid input")
        continue
    if (largest and smallest) is None :
        largest = fnum
        smallest = fnum
    if smallest > fnum :
        smallest = fnum
        #print("current small:",smallest)
    if largest < fnum :
        largest = fnum
        #print("current large :",largest)
        
print("Maximum is", largest)
print("Minimum is", smallest)
