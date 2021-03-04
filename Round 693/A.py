def calc(num):
	count = 1
	while num%2==0:
		count *= 2
		num = num//2
	return count

for nt in range(int(input())):
	w,h,n = map(int,input().split())
	ans = calc(w) * calc(h)
	if ans>=n:
		print ("YES")
	else:
		print ("NO")