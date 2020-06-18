n = int(input())
a = list(map(int,input().split()))
count = a[0]
ind = [1]
for i in range(1,n):
	if a[i]<=a[0]//2:
		count += a[i]
		ind.append(i+1)
if count>=(sum(a)//2+1):
	print (len(ind))
	print (*ind)
else:
	print (0)