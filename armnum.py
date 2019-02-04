mun = int(input())
length = len(str(mun))
mus = 0
temp = mun
while(temp != 0):
	mus = mus + ((temp % 10) ** length)
	temp = temp // 10
if mus == mun:
	print("yes")
else:
	print("no")
