for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	i=1
	j=n-1
	a=l[0]
	b=0
	ansa=l[0]
	ansb=0
	turn=0
	count=1
	while i<=j:
		if turn%2:
			start=0
			while start<=b and i<=j:
				start+=l[i]
				i+=1
			a=start
			ansa+=a
		else:
			start=0
			while start<=a and j>=i:
				start+=l[j]
				j-=1
			b=start
			ansb+=b
		count+=1
		turn=1-turn
	print (count,ansa,ansb)
