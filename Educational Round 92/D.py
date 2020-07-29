import sys
input = sys.stdin.readline

def intersection(a,b):
	if a[0]>=b[0] and a[1]<=b[1]:
		return -(a[1]-a[0])
	if b[0]>a[1]:
		return b[0]-a[1]
	elif b[1]<a[0]:
		return a[0]-b[1]
	if a[1]<b[1]:
		return b[0]-a[1]
	return a[0]-b[1]

# print (intersection((1,4),(5,15)))
# print (intersection((1,4),(4,15)))
# print (intersection((1,4),(2,15)))
# print (intersection((1,4),(1,15)))
# print (intersection((3,6),(1,15)))
# print (intersection((12,15),(4,15)))
# print (intersection((12,16),(4,15)))
# print (intersection((15,15),(4,15)))
# print (intersection((16,17),(4,15)))

def check(a,b):
	diff = intersection(a,b)
	if diff<0:
		if abs(diff)*n>=k:
			return True
	return False

for nt in range(int(input())):
	n,k = map(int,input().split())
	l1,r1 = map(int,input().split())
	l2,r2 = map(int,input().split())
	if r2-l2<r1-l1:
		minn = (l2,r2)
		maxx = (l1,r1)
	else:
		minn = (l1,r1)
		maxx = (l2,r2)
	if check(minn,maxx):
		print (0)
		continue

	diff = intersection(minn,maxx)
	one = abs(minn[0]-maxx[0]) + abs(minn[1]-maxx[1])
	r = (min(minn[0],maxx[0]),max(minn[1],maxx[1]))
	if diff<0:
		k -= abs(diff)*n
		done = r[1]-r[0]+diff
	else:
		done = r[1]-r[0]

	if one>=2*done:
		print (max(0,one+2*(k-done)))
		continue

	if done*n<=k:
		print (max(0,(one*n+2*(k-done*n))))
		continue

	left = k%done
	ans = (k//done)*one
	if diff<0:
		print (ans+left)
	else:
		if ans!=0:
			print (min(ans+2*left,ans+diff+left))
		else:
			print (ans+diff+left)
