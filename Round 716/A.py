import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = "NO"
	for i in a:
		if i**0.5 != int(i**0.5):
			ans = "YES"
			break
	print (ans)
