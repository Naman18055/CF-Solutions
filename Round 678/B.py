def isPrime(num):
	for i in range(2,num):
		if num%i==0:
			return False
	return True

def next_prime(num):
	for i in range(num, 10000):
		if isPrime(i) and not isPrime(i-num+1):
			return i

for nt in range(int(input())):
	n = int(input())
	ans = [[1 for i in range(n)] for j in range(n)]
	p = next_prime(n)
	for i in range(n-1):
		ans[i][-1] = p-(n-1)
		ans[-1][i] = p-(n-1)
	p = next_prime(sum(ans[-1][0:-1])+1)
	ans[-1][-1] = p - (sum(ans[-1][0:-1]))
	for i in ans:
		print (*i)