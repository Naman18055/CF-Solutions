import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
s1 = sum(a[0:n//2])
s2 = sum(a[n//2:])
print ((s1**2)+(s2**2))