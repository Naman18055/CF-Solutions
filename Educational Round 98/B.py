import sys
import math
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	print (max(max(a), math.ceil(sum(a)/(n-1)))*(n-1)-sum(a))