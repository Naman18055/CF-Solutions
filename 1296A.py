for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if sum(l)%2:
		print ("YES")
		continue
	odd,even=0,0
	for i in l:
		if i%2:
			odd=1
		else:
			even=1
	if odd==0 or even==0:
		print("NO")
	else:
		print ("YES")
