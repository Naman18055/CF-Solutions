n1, n2, n3 = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))
s = sum(a)+sum(b)+sum(c)
minn = 10**18
minn = min(minn, a[0]+min(b[0], c[0]), sum(a))
minn = min(minn, b[0]+min(a[0], c[0]), sum(b))
minn = min(minn, c[0]+min(a[0], b[0]), sum(c))

print (s-(2*minn))