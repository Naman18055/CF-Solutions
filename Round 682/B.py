mod = 10**9+7
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if len(set(a))==n:
		print ("NO")
	else:
		print ("YES")