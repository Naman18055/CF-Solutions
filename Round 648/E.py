import sys
input = sys.stdin.readline

def calc(arr):
	v = max(1,len(arr)-2)
	ans = 0
	for i in range(m):
		count = 0
		for j in range(len(arr)):
			if arr[j][i]=="1":
				count += 1
		if count>=v:
			ans += 2**(m-i-1)
	return ans

n = int(input())
a = sorted(list(map(int,input().split())))
a = a[::-1]
if n==1:
	print (a[0])
	exit()
if n==2:
	print (a[0]|a[1])
	exit()
ans = 0
for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			ans = max(ans,a[i]|a[j]|a[k])
print (ans)