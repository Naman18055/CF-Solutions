import sys

def askquery(i, j, op):
	print (op, i+1, j+1)
	sys.stdout.flush()
	return int(input())

n = int(input())
x1 = askquery(0, 1, "XOR")
x2 = askquery(1, 2, "XOR")
a = x1 + 2*(askquery(0, 1, "AND"))
b = x2 + 2*(askquery(1, 2, "AND"))
c = (x1^x2) + 2*(askquery(0, 2, "AND"))
# print (a, b, c)
ans = ["!"]
ans.append((a-b+c)//2)
ans.append(a-ans[-1])
ans.append(b-ans[-1])
for i in range(3,n):
	x = askquery(0, i, "XOR")
	ans.append(x^ans[1])
print (*ans)
