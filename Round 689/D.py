def find_sum(arr):
	if len(arr)==1:
		s.append(arr[0])
		return 
	elif len(arr)==0:
		return 
	elif len(set(arr)) == 1:
		s.append(sum(arr))
		return 
	s.append(sum(arr))
	a, b = [], []
	for i in arr:
		if i<=(arr[0]+arr[-1])//2:
			a.append(i)
		else:
			b.append(i)
	find_sum(a)
	find_sum(b)


for nt in range(int(input())):
	n, q = map(int,input().split())
	a = sorted(list(map(int,input().split())))
	s = []
	find_sum(a)
	s = set(s)
	for i in range(q):
		summ = int(input())
		if summ in s:
			print ("Yes")
		else:
			print ("NO")
