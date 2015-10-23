fname = raw_input("Enter a file name: ")
try: 
    fhand = open(fname)
except:
    print 'File Cannot be opened:', fname
    exit ()
count = 0
sum = 0
for line in fhand :
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    print line
    value = line [20: ]
    
count = count +1

