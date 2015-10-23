fname = raw_input("Enter file: ")
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname 
    end()

handle = open(fname,'r')
text = handle.read()
words = text.split()

wordslist = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words ==[]: continue 
    if words[0] != 'From' : continue
    #print words [1]
    
counts = dict()    
for word in words:
    if word in words: continue
    wordslist.append(word)
    counts[word] = counts.get(word,0)+1
print counts
    
bigcount = None
bigsend = None
for word.count in counts.items():
    if bigcount is None or count > bigcount:
        bigsend = word
        bigcount = count

print bigsend, bigcount