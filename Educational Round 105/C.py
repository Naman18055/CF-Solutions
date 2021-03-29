from bisect import bisect_left
def calc(a, b):
	if len(a)==0 or len(b)==0:
		return 0
	n, m = len(a)-1, len(b)-1
	ans = 0
	p = 0
	while n >= 0 and m >= 0:
		if a[n] > b[m]:
			n -= 1
			continue
		c = n + 1
		ind = bisect_left(b, b[m]-c+1)
		c2 = m - ind + 1 
		ans = max(ans, p+c2)
		if a[n] == b[m]: p += 1 
		m -= 1
	return ans


for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	ans = calc([i for i in a if i>0], [i for i in b if i>0])
	ans += calc([-i for i in a if i<0][::-1], [-i for i in b if i<0][::-1])
	print (ans)