mod = 998244353
w,h = map(int,input().split())
print ((4*(pow(2,w+h-2,mod)))%mod)