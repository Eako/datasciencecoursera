fname = raw_input("Enter a file name: ")
fhand = open(fname)
for line in fhand :
    line = line.rstrip().upper()
    print line
