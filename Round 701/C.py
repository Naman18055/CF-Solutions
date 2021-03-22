for nt in range(int(input())):
	x, y = map(int,input().split())
	ans = 0
	for i in range(1, int(x**0.5)+1):
		ans+=max(min(y,x//i-1)-i,0);
	print (ans)