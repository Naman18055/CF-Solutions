def calc(num):
	p = []
	for i in range(1,int(num**0.5)+1):
		if num%i==0:
			p.append(i)
			p.append(num//i)
	return p

def solve(diff):
	ans = []
	i = 0
	while len(ans)<n and (not ans or ans[-1]!=y):
		ans.append(x+i*diff)
		i += 1

	# print (diff,ans)

	i = 1
	flag = 0
	while len(ans)<n and (ans[-1]>0):
		ans.append(x-i*diff)
		flag = 1
		i += 1
	if ans[-1]<=0:
		ans.pop()

	i = 1
	while len(ans)<n:
		ans.append(y+i*diff)
		i += 1

	if y not in ans:
		return [10**18]

	return ans

for nt in range(int(input())):
	n,x,y = map(int,input().split())
	f = calc(y-x)
	m = 10**18
	for i in f:
		arr = solve(i)
		if max(arr)<m:
			ans = arr
			m = max(arr)

	print (*ans)