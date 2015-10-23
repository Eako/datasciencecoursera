counts = dict()
fname = raw_input("Enter file: ")
try:
	fhand = open(fname)
except:
    print 'File cannot be opened:',fname 
    end()

words = fname.split()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words ==[]: continue 
    if words[0] != 'From' : continue
print 'Words;', words