
dean=raw_input()
i=0
try:
    float(dean)
    i+=1
    print "yes"
except ValueError:
    pass
if i<1:
    if dean.isdigit():
        print "yes"
    else:
        print "No"
