import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	s = sum(a)
	if s%n!=0:
		print (-1)
		continue
	m = s//n
	num = a[0]
	ans = []
	for i in range(1,n):
		if a[i]%(i+1)==0:
			ans.append([i+1,1,a[i]//(i+1)])
			num += a[i]
			a[0] += (i+1)*(a[i]//(i+1))
		else:
			ans.append([1,i+1,(i+1)-a[i]%(i+1)])
			ans.append([i+1,1,a[i]//(i+1)+1])
			num += a[i]
			a[0] -= (i+1)-a[i]%(i+1)
			a[0] += (i+1)*(a[i]//(i+1)+1)
		a[i] = 0

	# print (a[0])
	for i in range(1,n):
		ans.append([1,i+1,m])


	print (len(ans))
	for i in ans:
		print (*i)
