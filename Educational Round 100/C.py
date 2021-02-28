import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = [[0, 0]]
	for i in range(n):
		a.append(list(map(int,input().split())))
	a.append([10**10, 0])
	curr = 0
	i = 1
	ans = 0
	free = 1
	t = 0
	prev = 0
	changed = 0
	target = 0
	while i<n+1:
		time_left = a[i+1][0] - a[i][0] 
		if a[i][0]>=t:
			curr = target
			changed = 1
			free = 1

		if free:
			target = a[i][1]
			t = abs(a[i][1] - curr) + a[i][0]
			free = 0

		if not changed:
			if target>curr:
				curr += (a[i][0]-a[i-1][0])
			else:
				curr -= (a[i][0]-a[i-1][0])
		else:
			changed = 0

		x = a[i][1]
		if (abs(x-curr)+abs(x-target)==abs(target-curr)) and time_left>=abs(x-curr):
			ans += 1

		# print (ans, curr, target, t, time_left)
		i += 1

	print (ans)



# 1
# 28
# 61 -45
# 148 71
# 205 85
# 236 95
# 284 98
# 294 30
# 315 24
# 409 2
# 490 24
# 570 -43
# 584 -3
# 599 -15
# 664 23
# 735 -68
# 751 -56
# 807 -46
# 844 39
# 880 38
# 902 55
# 926 29
# 1005 -39
# 1104 56
# 1111 66
# 1140 -42
# 1240 -78
# 1266 -35
# 1268 -33
# 1281 -90









