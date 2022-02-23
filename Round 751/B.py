import sys
from collections import Counter
input = sys.stdin.readline

def calculateStep(arr):
	c = Counter(arr)
	res = []
	for i in arr:
		res.append(c[i])
	return res


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	q = int(input())
	steps = [a]
	nextStep = calculateStep(steps[-1])
	while nextStep!=steps[-1]:
		steps.append(nextStep)
		nextStep = calculateStep(steps[-1])
	for i in range(q):
		x, k = map(int,input().split())
		if k<len(steps):
			print (steps[k][x-1])
		else:
			print (steps[-1][x-1])