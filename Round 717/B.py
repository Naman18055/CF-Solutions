import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	xor = 0
	for i in a:
		xor = xor^i
	if xor==0:
		print ("YES")
		continue
	curr1 = 0
	ans = "NO"
	for i in range(n):
		curr1 = curr1^a[i]
		curr2 = 0
		if curr1==xor:
			for j in range(i+1, n):
				curr2 = curr2^a[j]
				if curr2==xor:
					ans = 'YES'
					break
	print (ans)