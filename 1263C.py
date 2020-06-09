for nt in range(int(input())):
	n = int(input())
	a = [0]
	for i in range(1,int(n**0.5)+1):
		a.append(n//i)
		a.append(i)
	a = sorted(list(set(a)))
	print (len(a))
	print (*a)