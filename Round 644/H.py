for nt in range(int(input())):
	n,m = map(int,input().split())
	r = []
	for i in range(n):
		r.append(int(input(),2))
	r.sort()
	left = 2**m-n
	med = (left-1)//2
	for i in range(n):
		if r[i]<=med:
			med+=1
	ans = bin(med)[2:]
	ans = "0"*(m-len(ans))+ans
	print (ans)
