for nt in range(int(input())):
	n = int(input())
	if not n%2:
		print (*([i for i in range(1,n+1)][::-1]))
	else:
		ans = [i for i in range(1, n+1)]
		ans = ans[::-1]
		ans[0], ans[n//2] = ans[n//2], ans[0]
		print (*ans)