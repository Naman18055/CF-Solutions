def sieve(n):
	prime = [-1]*(n+1)
	for i in range(2,n+1):
		if prime[i]==-1:
			for j in range(i,n+1,i):
				prime[j] = i
	return prime


p = sieve(10**5)
prime = []
for i in range(len(p)):
	if p[i]==i:
		prime.append(i)
for nt in range(int(input())):
	n = int(input())
	div = []
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			div.append(i)
			if i!=n//i:
				div.append(n//i)
	# print (div)
	if len(div)==2:
		print (div[0], div[1], n)
		print (1)
	else:
		p = []
		for i in prime:
			if n%i==0:
				p.append(i)
		ans = []
		for i in range(len(p)-1):
			ans.append(p[i])
			ans.append(p[i]*p[i+1])
		ans.append(p[-1])
		ans.append(p[-1]*p[0])
		done = set(ans)
		inc = {}
		for i in div:
			if i not in done:
				for j in p:
					if i%j==0:
						if j not in inc:
							inc[j] = [i]
						else:
							inc[j].append(i)
						break
		f = []
		for i in range(0,len(ans),2):
			f.append(ans[i])
			if ans[i] in inc:
				f.extend(inc[ans[i]])
			f.append(ans[i+1])
		f.append(n)
		print (*f)
		print (0)





