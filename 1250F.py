n = int(input())
for i in range(int(n**0.5)+1,0,-1):
	if n%i==0:
		print (2*(i+n//i))
		exit()