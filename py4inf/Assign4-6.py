#overtime payment calculator with functions
def computepay (h, r):
    if h <= 40:             #normal compensation
        p = h * r
    else:                     #overtime compensation
        p = r * 40 + (r * 1.5 * (h - 40))
    return p
try: 
    inpt = raw_input("Enter Hours:")
    hours = float (inpt)
    inpt = raw_input("Enter Rate:")
    rate = float(inpt)
except:
    print "error, please enter numeric input"
    quit ()


pay = computepay (hours, rate)
print "Pay", float(pay)