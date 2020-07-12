n = int(input())
a = list(map(int,input().split()))
a = a + a + a
b = max(a)
for i in range(n,2*n):
	if a[i]==b:
		ind = i
		break

ans = a[ind]
count = 0
i = ind-2
j = ind+2
while count != n//2:
	# print (a,i,j)
	if a[i+1] < a[j-1]:
		ans += a[i]
		i -= 2
	elif a[j-1] < a[i+1]:
		ans += a[j]
		j += 2
	else:
		if a[j]<a[i]:
			ans += a[i]
			i -= 2
		else:
			ans += a[j]
			j += 2
	count += 1
print (ans)
