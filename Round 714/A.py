for nt in range(int(input())):
	n, k = map(int,input().split())
	if k>=(n+1)//2:
		print (-1)
		continue
	if n==1:
		print (1)
		continue
	i = 2
	j = n
	ans = [1]
	turn = 1
	while k:
		if turn:
			ans.append(j)
			j -= 1
			k -= 1
		else:
			ans.append(i)
			i += 1
		turn = 1-turn
	ans.append(i)
	i += 1

	for j in range(n-len(ans)):
		ans.append(i)
		i += 1
	print (*ans)