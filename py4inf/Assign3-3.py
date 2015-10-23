#enter score to get alpha grade per scale

try:    
    input = raw_input('Please enter score from 0.0 to 1.0: ')
    numscore = float (input)
    if numscore >= 1.0:
        print 'Error, invalid score'
    elif numscore >= 0.9:
        print 'A'
    elif numscore >= 0.8:
        print 'B'
    elif numscore >= 0.7:
        print 'C'
    elif numscore >= 0.6:
        print 'D'
    elif numscore < 0.6:
        print 'F'
except:
    print 'Error, invalid score'   
    