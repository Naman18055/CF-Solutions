def correct(a,b,c):
	if a+b<=c or b+c<=a or a+c<=b:
		return False
	return True

n = int(input())
ans = 0
for i in range(2,n+1):
	for j in range(i+1,n+1):
		s = i^j
		if (s>j and s<=n) and correct(i,j,i^j):
			ans += 1
print (ans)