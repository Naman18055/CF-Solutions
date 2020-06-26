def func(n):
	return sum(map(int,list(str(n))))

def calc(n):
	x = n//9
	return int(str(n%9)+"9"*x)

for nt in range(int(input())):
	n,k = map(int,input().split())
	k += 1
	s = 0
	for i in range(k):
		s += func(i)
	print (s)
	# ind = 10**18
	# while True:
	# 	if (n-s)%k == 0:
	# 		ind = s
	# 		break
	# 	s -= 9
	# if ind==10**18:
	# 	print (-1)
	# 	continue
	# minn = calc((n-ind)//k)
	# print (minn)
	# # (n-k*func(a)) = s


	for i in range(100):
		s = 0
		for j in range(k):
			s += func(i+j)-func(i)
		print (i,s)