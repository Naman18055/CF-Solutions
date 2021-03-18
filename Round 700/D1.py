n = int(input())
a = list(map(int,input().split()))
x, y = [0], [0]
for i in range(n):
	if a[i]!=x[-1] and a[i]!=y[-1]:
		if i<n-1 and a[i+1]==x[-1]:
			x.append(a[i])
		else:
			y.append(a[i])
	elif a[i]!=y[-1]:
		y.append(a[i])
	elif a[i]!=x[-1]:
		x.append(a[i])

print (len(x)+len(y)-2)

