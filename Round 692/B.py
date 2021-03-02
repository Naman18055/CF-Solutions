def is_fair(n):
	x = n
	while x > 0:
		d = (x%10)
		if d != 0 and n % d != 0:
			return False
		x = x // 10
	return True

t = int(input())
for i in range(t):
	i = int(input())
	while True:
		if is_fair(i):
			print(i)
			break
		i += 1
