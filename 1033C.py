n = int(input())
a = list(map(int,input().split()))
ans = [-1]*n
loc = {}
for i in range(n):
	loc[a[i]] = i
for i in range(n):
	if a[i]>i and a[i]>=n-i:
		ans[i] = "B"
prev = 0
while ans.count(-1)!=prev:
	prev = ans.count(-1)
	for i in range(n):
		if ans[i]==-1:
			for j in range(i%a[i],n,a[i]):
				if a[j]>a[i] and ans[j]=="B":
					ans[i] = "A"
					break
	# print (ans)
while ans.count(-1)!=0:
	for i in range(n):
		if ans[i]==-1:
			ans[i] = "B"
			for j in range(i%a[i],n,a[i]):
				if a[i]>=a[j]:
					continue
				if ans[j]=="B":
					ans[i]="A"
					break
				elif ans[j]==-1:
					ans[i] = -1
					break
			# print (ans)
for i in ans:
	print (i,end="")
print ()

