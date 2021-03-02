for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	m = int(input())
	b = list(map(int,input().split()))
	pa, pb = [a[0]], [b[0]]
	for i in range(1, n):
		pa.append(pa[-1] + a[i])
	for i in range(1, m):
		pb.append(pb[-1] + b[i])
	print (max(max(pa), 0)+max(max(pb), 0))