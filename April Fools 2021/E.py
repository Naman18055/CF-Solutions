n, m = map(int,input().split())
a = []
for i in range(n):
	a.append(list(input()))
t = 1
curr = [0, 0]
if a[curr[0]][curr[1]]=="*":
	ans = 1
else:
	ans = 0
while curr!=[n-1, m-1]:
	if t:
		if curr[0]!=n-1:
			curr[0] += 1
			t = 1-t
		else:
			curr[1] += 1
	else:
		if curr[1]!=m-1:
			curr[1] += 1
			t = 1-t
		else:
			curr[0] += 1
	if a[curr[0]][curr[1]]=="*":
		ans += 1
# if a[n-1][m-1]=="*":
	# ans -= 1

print (ans)
# t = 0
# curr = [0, 0]
# if a[curr[0]][curr[1]]=="*":
# 	c = 1
# else:
# 	c = 0
# while curr!=[n-1, m-1]:
# 	if t:
# 		if curr[0]!=n-1:
# 			curr[0] += 1
# 			t = 1-t
# 		else:
# 			curr[1] += 1
# 	else:
# 		if curr[1]!=m-1:
# 			curr[1] += 1
# 			t = 1-t
# 		else:
# 			curr[0] += 1
# 	if a[curr[0]][curr[1]]=="*":
# 		c += 1

# print (max(ans, c))