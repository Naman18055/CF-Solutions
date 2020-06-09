import math
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=[-1]*n
	color=1
	primes=[2,3,5,7,11,13,17,19,23,29,31,37]
	for i in range(12):
		flag=False
		for j in range(n):
			if ans[j]==-1:
				if l[j]%primes[i]==0:
					ans[j]=color
					flag=True
		if flag:
			color+=1
		
	print (len(set(ans)))
	print (*ans)