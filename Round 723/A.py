import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	ans = []
	i = 0
	j = 2*n-1
	while len(ans)!=2*n:
		ans.append(a[i])
		i += 1
		ans.append(a[j])
		j -= 1
	print (*ans)