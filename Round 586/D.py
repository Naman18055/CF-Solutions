n = int(input())
a = list(map(int,input().split()))
bit = [0]*64
b = []
for i in a:
	k = i
	count = 0
	while not k%2:
		k = k//2
		count += 1
	b.append(count)
	bit[count] += 1

print (n-max(bit))
for i in range(n):
	if b[i]!=bit.index(max(bit)):
		print (a[i],end=" ")
print ()