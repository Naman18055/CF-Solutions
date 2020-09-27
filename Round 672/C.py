import sys
input = sys.stdin.buffer.readline

# input = raw_input
def change(ind,sign):
	global ans
	ind -= 1
	if ind==0:
		if a[ind]>a[ind+1]:
			ans += sign*a[ind]
		return
	if ind==n-1:
		if a[ind]>a[ind-1]:
			ans += sign*a[ind]
		return
	if (a[ind]>a[ind-1]) and (a[ind]>a[ind+1]):
		ans += sign*a[ind]
	if (a[ind]<a[ind-1]) and (a[ind]<a[ind+1]):
		ans -= sign*a[ind]


def change2(l,r,sign):
	if l==r:
		return
	if l+1==r:
		if l!=1:
			change(l-1,sign)
		change(l,sign)
		change(l+1,sign)
		if r!=n:
			change(r+1,sign)
		return 

	if l!=1:
		change(l-1,sign)
	if r!=n:
		change(r+1,sign)
	change(l,sign)
	change(l+1,sign)
	change(r,sign)
	if l+2!=r:
		change(r-1,sign)


for nt in range(int(input())):
	n,q = map(int,input().split())
	a = list(map(int,input().split()))
	if n==1:
		print (a[0])
		for i in range(q):
			l,r = map(int,input().split())
			print (a[0])
		continue
	inc = -1
	for i in range(1,n):
		if a[i]>a[i-1]:
			inc = 1
			break
		elif a[i]<a[i-1]:
			inc = 0
			break

	if inc==-1:
		print (a[0])
		for i in range(q):
			l,r = map(int,input().split())
			print (a[0])
		continue
	elif inc:
		ans = 0
	else:
		ans = a[0]
	for i in range(1,n):
		if a[i]>a[i-1] and inc:
			continue
		elif a[i]>a[i-1]:
			ans -= a[i-1]
			inc = 1
		elif a[i]<a[i-1] and inc:
			ans += a[i-1]
			inc = 0
		else:
			continue
	if inc:
		ans += a[-1]


	print (ans)
	for i in range(q):
		l,r = map(int,input().split())
		change2(l,r,-1)
		a[l-1], a[r-1] = a[r-1], a[l-1]
		change2(l,r,1)
		print (ans)




