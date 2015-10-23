#extract portion of information & send as floating point

data = 'X-DSPAM-Confidence: 0.8475 '
beginpos = data.find(":")
#print beginpos

endpos = data.find("5", beginpos)
#print endpos

input = data[beginpos+2:endpos+1]
print float(input)