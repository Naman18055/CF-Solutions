s = input()
n = len(s)
done = {}
a = 0
f = []
while True:
	i=0
	j=n-1
	count = 0
	ans = []
	while i<j:
		while i<j and (i in done or s[i]!="("):
			i+=1
		while j>i and (j in done or s[j]!=")"):
			j-=1
		if i==n or j==i:
			break
		else:
			done[i] = 1
			done[j] = 1
			ans.append(i+1)
			ans.append(j+1)
			count += 2
		# print (i,j,ans)
	if count==0:
		break
	a += 1
	f.append(ans)
print (a)
for i in range(a):
	print (len(f[i]))
	print (*(sorted(f[i])))