n = int(input())
a = list(map(int,input().split()))
d = {}
for i in range(n):
	for j in range(i):
		if a[i]+a[j] not in d:
			d[a[i]+a[j]] = (i, j)
		else:
			s = a[i]+a[j]
			x = d[s]
			if i not in x and j not in x:
				print ("YES")
				print (x[0]+1, x[1]+1, i+1, j+1)
				exit()
print ("NO")
