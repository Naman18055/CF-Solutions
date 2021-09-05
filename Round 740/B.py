for nt in range(int(input())):
	x, y = map(int,input().split())
	ans = []
	if (x+y)%2:
		for z in range(x+y+1):
			n = ((x-y+1)/2 + z)/2
			m = (z - (x-y+1)/2)/2
			if n==int(n) and m==int(m) and n>=0 and m>=0 and n<=(x+y)//2+1 and m<=(x+y)//2:
				ans.append(z)
				continue
			n = ((x-y-1)/2 + z)/2
			m = (z - (x-y-1)/2)/2
			if n==int(n) and m==int(m) and n>=0 and m>=0 and n<=(x+y)//2 and m<=(x+y)//2+1:
				ans.append(z)
				continue
	else:
		p = (x+y)//2
		for z in range(x+y+1):
			n = ((x-y)/2 + z)/2
			m = (z - (x-y)/2)/2
			if n==int(n) and m==int(m) and n>=0 and m>=0 and n<=(x+y)//2 and m<=(x+y)//2:
				ans.append(z)
	ans = sorted(list(set(ans)))
	print (len(ans))
	print (*ans)


