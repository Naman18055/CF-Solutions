def f(num):
	x = m//num
	return x*num

def s(num):
	x = (m-1)//num+1
	return x*num

def calc(num):
	x = l
	y = l + abs(num)
	if num>0:
		return y,x
	return x,y

for nt in range(int(input())):
	l,r,m = map(int,input().split())
	for i in range(l,r+1):
		first = f(i)
		second = s(i)
		if first and abs(m-first)<=(r-l):
			ans = [i,first]
			break
		if abs(m-second)<=(r-l):
			ans = [i,second]
			break
	diff = m - ans[1]
	b,c = calc(diff)
	print (ans[0],b,c)

