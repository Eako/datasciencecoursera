#loop program reads numbers to find min & max values
smallest = None
largest = None
while True:
    input = raw_input ("Enter a number: ")
    if input == "done" : break
    if len(input) < 1 : break  #checks for empty line to end
    
    try:
        num = float (input)
    except: 
        print "Invalid input"
        continue            #restarts loop to get new data
    for itervar in [input]:
        if input is None or itervar > largest:
            largest = itervar
            #return largest
    
    for itervar in [input]:
        if smallest is None:
            smallest = itervar
        elif itervar < smallest:
            smallest = itervar
print "Maximum is ",largest
print "Minimum is ",smallest
#enter ends the program to get min & max values

