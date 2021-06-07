import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	left, right = [-10**18], [10**18]
	s = a[0]
	ans = "YES"
	for i in a[1:]:
		if i>s:
			if i>right[-1]:
				ans = "NO"
				break
			left.append(s)
			s = i
			if i==right[-1]:
				right.pop()
		elif i<s:
			if i<left[-1]:
				ans = "NO"
				break
			right.append(s)
			s = i
			if i==left[-1]:
				left.pop()
	print (ans)
