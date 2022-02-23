import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if a.count(0)==n:
		print (*[i for i in range(1, n+1)])
		continue
	b = []
	for i in a:
		b.append(list("0"*(32-len(bin(i)[2:]))+bin(i)[2:]))

	countOnes = [0]*32
	for i in range(32):
		for j in range(n):
			if b[j][i]=="1":
				countOnes[i] += 1

	factors = []
	for i in countOnes:
		if i!=0:
			for j in range(1, int(i**0.5)+1):
				if i%j==0:
					factors.append(j)
					factors.append(i//j)
			break
	res = []
	for i in factors:
		flag = True
		for j in countOnes:
			if j!=0 and j%i!=0:
				flag = False
				break
		if flag:
			res.append(i)
	print (*sorted(list(set(res))))







