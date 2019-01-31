bol = int(input())
temp = bol
ran = 0
while temp != 0:
	ran = (ran * 10) + (temp % 10)
	temp = temp // 10
if bol == ran:
	print("yes")
else:
	print("no")
