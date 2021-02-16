for nt in range(int(input())):
	n = int(input())
	div = []
	for i in range(2, int(n**0.5)+1):
		if n%i==0:
			div.append(i)
			if n//i!=i:
				div.append(n//i)
	if not div:
		print (1)
		print (n)
		continue

	count = {}
	i = 0
	k = n
	while i<len(div):
		k = n
		c = 0
		while k%div[i]==0:
			k = k//div[i]
			c += 1
		count[div[i]] = c
		i += 1
	maxx = 0
	num = -1
	# print (count)
	for i in count:
		if (n//(i**(count[i]-1)))%i==0 and count[i]>maxx:
			maxx = count[i]
			num = i

	if num==-1:
		print (1)
		print (n)
		continue

	ans = []
	while n%num==0:
		ans.append(num)
		n = n//num
	ans[-1] = ans[-1]*n
	print (len(ans))
	print (*ans)

