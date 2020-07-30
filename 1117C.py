def check(num):
	if num%n==0:
		y3 = pref[-1][0]*(num//n) + y1
		x3 = pref[-1][1]*(num//n) + x1
	else:
		y3 = pref[-1][0]*(num//n) + pref[num%n-1][0] + y1
		x3 = pref[-1][1]*(num//n) + pref[num%n-1][1] + x1
	if abs(x3-x2) + abs(y3-y2)<=num:
		return True
	return False



x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
n = int(input())
s = input()
pref = [[0,0]]
if s[0]=="U":
	pref[0][0] += 1
elif s[0]=="D":
	pref[0][0] -= 1
elif s[0]=="R":
	pref[0][1] += 1
else:
	pref[0][1] -= 1
for i in range(1,n):
	new = [pref[-1][0],pref[-1][1]]
	if s[i]=="U":
		new[0] += 1
	elif s[i]=="D":
		new[0] -= 1
	elif s[i]=="R":
		new[1] += 1
	else:
		new[1] -= 1
	pref.append(new)

# print (pref)
low = 0
high = 10**18
while low<high:
	mid = (low+high)//2
	if check(mid):
		high = mid - 1
	else:
		low = mid + 1
if low>10**15:
	print (-1)
	exit()
if check(low):
	print (low)
else:
	print (low+1)