import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n,w = map(int,input().split())
	a = list(map(int,input().split()))
	s = 0
	b = []
	for i in range(n):
		if (w+1)//2 <= a[i] <= w:
			print(1)
			print(i + 1)
			break
		elif a[i] < (w+1)//2:
			s += a[i]
			b.append(i + 1)
			if s >= (w+1)//2:
				print(len(b))
				print(*b)
				break
	else:
		print(-1)