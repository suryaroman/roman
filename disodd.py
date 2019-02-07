bob,las=map(int,input().split())
c=[]
for i in range(bob+1,las):
  if(i%2!=0):
    #print(i,end=" ")
    c.append(i)
print(*c)
