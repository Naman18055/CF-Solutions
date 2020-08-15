n = int(input())
s = input()
z = s.count("z")
o = s.count("o")
ans = [1]*(o-z)+[0]*z
print (*ans)