# ORIGINAL --

# import sys
# input = sys.stdin.readline
# from collections import Counter

# def calc(n):
# 	num = 1
# 	for i in range(2, int(n**0.5)+1):
# 		c = 0
# 		while n%i==0:
# 			c += 1
# 			n = n//i
# 		if c%2==1:
# 			num *= i
# 	num *= n
# 	return num

# for nt in range(int(input())):
# 	n = int(input())
# 	a = list(map(int,input().split()))
# 	for i in range(n):
# 		a[i]=calc(a[i])
# 	d = Counter(a)

# 	a = 0
# 	b = 0
# 	maxx = 0
# 	for i in d:
# 		maxx = max(maxx, d[i])
# 		if i>1 and d[i]%2!=0:
# 			a = max(a, d[i])
# 		else:
# 			b += d[i]
	
# 	for i in range(int(input())):
# 		x = int(input())
# 		if x==0:
# 			print (maxx)
# 		else:
# 			print (max(a, b))

# COPIED --

from collections import defaultdict

import sys
input = sys.stdin.buffer.readline
def print(val):
    sys.stdout.write(str(val)+'\n')

primefactors = defaultdict(list)
primes = []
for n in range(2, 10 ** 6 + 1):
    if primefactors[n]:
        continue
    else:
        primes.append(n)
        k = n
        while k < 10 ** 6 + 1:
            primefactors[k].append(n)
            k += n

T = int(input())
for case in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0, 0]
    cnt = defaultdict(int)
    for k in a:
        divk = 1
        for p in primefactors[k]:
            valp = 0
            while k % p == 0:
                k //= p
                valp ^= 1
            divk*=(p**valp)
        cnt[divk] += 1
    ans[0] = max(cnt.values())

    if cnt[1] % 2:
        cnt2 = [cnt[1]]
    else:
        cnt2 = [0]

    for k in cnt.values():
        if k % 2:
            cnt2.append(k)
        else:
            cnt2[0] += k
    ans[1] = max(cnt2)

    q = int(input())
    for _ in range(q):
        w = int(input())
        if w == 0:
            print(ans[0])
        else:
            print(ans[1])
