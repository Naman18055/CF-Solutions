import sys
input = sys.stdin.readline

def solve(a, b):
	a = bin(a)[2:]
	b = bin(b)[2:]
	a = "0"*(32-len(a))+a
	b = "0"*(32-len(b))+b
	s = ""
	# print(a)
	# print(b)
	for i in range(32):
		if a[i]=="1" and b[i]=="0":
			s += "1"
		else:
			s += "0"
	return int(s, 2)


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = [0]
	if n==1:
		print (*ans)
		continue
	ans.append(solve(a[0], a[1]))
	for i in range(2, n):
		ans.append(solve(ans[-1]^a[i-1], a[i]))
	print (*ans)