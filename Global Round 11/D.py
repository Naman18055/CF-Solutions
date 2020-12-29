def not_sorted(a):
	if a==sorted(a):
		return False
	return True

def apply(op):
	global a
	parts = []
	ind = 0
	for i in op:
		parts.append(a[ind:ind+i])
		ind += i
	parts = parts[::-1]
	a = []
	for i in parts:
		a.extend(i)

def clean(op):
	new = []
	for i in op:
		if i:
			new.append(i)
	if len(new)!=1:
		ans.append([len(new)]+new)

def apply_op(num, right):
	if right:
		loc = a.index(num)
		op = [1]*(n-num)
		op.append(loc - len(op) + 1)
		op.append(n - loc -1)
	else:
		loc = a.index(num)
		op = [loc]
		op.append(num - loc)
		op.extend([1]*(n-num))
	clean(op)
	apply(op)
	# print (op, num, right)
	# print (*a)



n = int(input())
a = list(map(int,input().split()))
num = n
right = 1
ans = []
while num and not_sorted(a):

	apply_op(num, right)
	right = 1-right
	num -= 1

print (len(ans))
for i in ans:
	print (*i)




