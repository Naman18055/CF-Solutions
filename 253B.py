import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
n = int(input())
a = list(map(int,input().split()))
a.sort()
maxx = 0
i,j = 0,0
while j<n:
	while j<n and a[j]<=2*a[i]:
		j += 1
	maxx = max(j-i,maxx)
	i += 1
print (n-maxx)