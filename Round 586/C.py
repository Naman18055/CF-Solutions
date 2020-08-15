s = input()
n = len(s)
print ("Mike")
minn = s[0]
for i in range(1,n):
	if s[i]>minn:
		print ("Ann")
	else:
		print ("Mike")
	minn = min(s[i],minn)
