for nt in range(int(input())):
	n,k = map(int,input().split())
	if sum(list(map(int,input().split())))==k:
		print ("YES")
	else:
		print ("NO")