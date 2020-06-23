
n,k,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
sm = sum(l)
ans = 0
for i in range(n+1):
	if sm*i > m:
		break
	m1 = m-sm*i
	cnt = [n-i]*(k)
	cur = 0
	res = (k+1)*i
	while m1 > 0:
		if cur >= k or l[cur] > m1:
			break
		x = min(m1//l[cur],cnt[cur])
		res += x
		m1 -= x*l[cur]
		cur += 1
	ans = max(res,ans)
print(ans)