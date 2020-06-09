import sys
input = sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
s=set()
ans=n+1
if (len(set(l))==n):
	print (0)
else:
	for i in range(n):
		t=s.copy()
		for j in range(n-1,i-1,-1):
			if l[j] not in t:
				t.add(l[j])
			else:
				if (j-i+1) < ans:
					ans = (j-i+1)
				break
		if (l[i]) not in s:
			s.add(l[i])
		else:
			break
	print (ans)

