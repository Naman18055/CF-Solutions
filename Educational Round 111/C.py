import sys
input = sys.stdin.readline

def correct(i, j):
	num = a[i:j]
	if len(num)==3:
		if (num[0]<=num[1] and num[1]<=num[2]) or (num[0]>=num[1] and num[1]>=num[2]):
			return False
		return True

	b = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
	for i in b:
		if (num[i[0]]<=num[i[1]] and num[i[1]]<=num[i[2]]) or (num[i[0]]>=num[i[1]] and num[i[1]]>=num[i[2]]):
			return False
	return True


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	for i in range(3, 5):
		for j in range(n-i+1):
			if correct(j, j+i):
				ans += 1
	print (ans + n + n-1)