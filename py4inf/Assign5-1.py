#loop program reads numbers & creates total, count & average

count = 0
total = 0
while True:
    input = raw_input ("Enter a number: ")
    if input == "done" : break
    if len(input) < 1 : break  #checks for empty line to end
    
    try:
        num = float (input)
    except: 
        print "Invalid input"
        continue            #restarts loop to get new data
    count = count + 1
    total = total + num
    print num, total, count
#enter ends the program to get average
print "DONE"
print "Average: ", total / count