for nt in range(int(input())):
	n = int(input())
	if n%2050!=0:
		print (-1)
		continue
	print (sum(list(map(int, list(str(n//2050))))))