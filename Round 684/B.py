for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	ind = ((n+1)//2-1)*k
	print (sum(a[ind::n-(ind//k)]))