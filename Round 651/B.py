import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	odd,even = [],[]
	for i in range(2*n):
		if a[i]%2:
			odd.append((a[i],i+1))
		else:
			even.append((a[i],i+1))
	ans = []
	# print (odd,even)
	for i in range(0,len(even)-1,2):
		ans.append((even[i][1],even[i+1][1]))
		if len(ans)==n-1:
			break
	for i in range(0,len(odd)-1,2):
		if len(ans)==n-1:
			break
		ans.append((odd[i][1],odd[i+1][1]))
	for i in ans:
		print (i[0],i[1])