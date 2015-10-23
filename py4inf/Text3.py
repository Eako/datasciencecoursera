#overtime payment calculator
inpt = raw_input("Enter Hours:")
hours = float (inpt)
inpt = raw_input("Enter Rate:")
rate = float(inpt)
if hours <= 40:             #normal compensation
   payrate = hours * rate
if hours > 40:              #overtime compensation
   payrate = rate * 40 + (rate * 1.5 * (hours - 40))

print "Pay:", float(payrate)
