s=input()
d=len(s)
count=0
for i in range(0,d):
	if(s[i]=='.'):
		count+=1
count+=1
print(count)
