#enter score to get alpha grade per scale
def computegrade (s):
    if s >= 1.0:
        g = 'Bad Score'
    elif s >= 0.9:
        g = 'A'
    elif s >= 0.8:
        g =  'B'
    elif s >= 0.7:
        g = 'C'
    elif s >= 0.6:
        g = 'D'
    elif s < 0.6:
        g = 'F'
    return g
        
try:    
    input = raw_input('Please enter score from 0.0 to 1.0: ')
    numscore = float (input)
except:
    print 'Error, invalid score'   
    quit ()

grade = computegrade (numscore)
print str(grade)