from collections import deque
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
q = deque()
prev = a[0]
count = 1
for i in range(1,n):
	if a[i]==prev:
		count += 1
	else:
		q.append([prev,count])
		prev = a[i]
		count = 1
q.append([prev,count])
j = len(q)-1
while k and j>0:
	# print (q,k)
	if q[0][1] < q[j][1]:
		x = q.popleft()
		diff = q[0][0]-x[0]
		if diff*x[1]<=k:
			k -= diff*x[1]
			q[0][1] += x[1]
			j -= 1
		else:
			q.appendleft([x[0] + k//x[1],x[1]])
			break
	else:
		x = q.pop()
		diff = x[0]-q[-1][0]
		if diff*x[1]<=k:
			k -= diff*x[1]
			q[-1][1] += x[1]
			j -= 1
		else:
			q.append([x[0] - k//x[1],x[1]])
			break
print (q[-1][0]-q[0][0])