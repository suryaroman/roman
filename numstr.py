roman=raw_input()
i=0
try:
    float(roman)
    i+=1
    print "yes"
except ValueError:
    pass
if i<1:
    if roman.isdigit():
        print "yes"
    else:
        print "No"
