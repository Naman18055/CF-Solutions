import heapq

n = int(input())
a = list(map(int,input().split()))
h = []
heapq.heapify(h)
ans = 0
c = 0
for i in a:
	if i>=0:
		c += i
		ans += 1
	else:
		if c+i>=0:
			c += i
			ans += 1
			heapq.heappush(h, i)
		else:
			if h:
				if h[0]<i:
					c -= heapq.heappop(h)
					heapq.heappush(h, i)
					c += i
print (ans)




