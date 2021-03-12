for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	suok = [True]
	sulft = [0]
	for i in range(n - 1, -1, -1):
		if not suok[-1] or a[i] < sulft[-1]:
			suok.append(False)
			sulft.append(0)
		else:
			suok.append(True)
			sulft.append(a[i] - sulft[-1])
	a.append(0)
	suok = suok[::-1]
	sulft = sulft[::-1]
	if suok[0] and sulft[0] == 0:
		print("YES")
		continue
	prlft = 0
	win = False
	for i in range(n - 1):
		a[i], a[i + 1] = a[i + 1], a[i]
		if suok[i + 2] and a[i] >= prlft and a[i + 1] >= (a[i] - prlft) and a[i + 1] - (a[i] - prlft) == sulft[i + 2]:
			win = True
			break
		a[i], a[i + 1] = a[i + 1], a[i]
		if a[i] < prlft:
			break
		prlft = a[i] - prlft
	print("YES" if win else "NO")