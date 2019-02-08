rey,mys=map(int,input().split())
c=[]
for i in range(rey+1, mys):
	dean=0
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				dean=1
		if(dean==0):
		    c.append(i)
print(*c)				
