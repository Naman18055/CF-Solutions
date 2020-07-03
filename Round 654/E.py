def places(num,v):
	if num>=v+n:
		return 0
	if num<v:
		return n
	return (n-(num-v))


def check(num):
	for i in range(n-1,-1,-1):
		count = max(0, places(b[i],num) - ((n-1)-i))
		# print (num,count)
		if count%p==0:
			return True
	return False

n,p = map(int,input().split())
a = list(map(int,input().split()))
b = sorted(a)
minn = b[0]
maxx = b[-1]
ans = []
for i in range(minn,maxx):
	if not check(i):
		ans.append(i)
print (len(ans))
print (*ans)