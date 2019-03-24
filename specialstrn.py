string = input()
alphabets = digits = special = 0
space=0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    elif(string[i]==' '):
    	space=space+1
    else:
        special = special + 1
print(special)        
