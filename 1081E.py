def perfect(num):
	return int(num**(0.5))==num**(0.5)

def check(num):
	for i in a:
		if not perfect(num):
			print (num)
			return False
		num += i
	if not perfect(num):
		return False
	return True

def subarray(num):
	i = 0
	j = 0
	s = 0
	while j<len(arr):
		s += arr[j]
		if arr[j]==num:
			return j
		if arr[j]>num:
			s -= arr[i]
			i += 1
		else:
			j += 1
	return -1

n = int(input())
a = list(map(int,input().split()))
ans = [-1]*(n+1)
for i in range(n-1,-1,-2):
	if a[i//2]%2:
		num = a[i//2]//2
		ans[i] = num**2
		ans[i+1] = (num+1)**2
	else:
		num = a[i//2]//2
		if num%2:
			print ("No")
			exit()
		ans[i] = ((num-1)//2)**2
		ans[i+1] = ((num-1)//2+2)**2
	# print (ans)
print (ans)
if sorted(ans)==ans:
	print ("Yes")
	print (ans[1],end=" ")
	for i in range(2,n+1):
		print (ans[i]-ans[i-1],end=" ")
	print ()
else:
	print ("No")





