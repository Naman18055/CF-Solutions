import math
for nt in range(int(input())):
	n = int(input())
	if n%2:
		print ("Bob")
		continue
	if math.log2(n)==int(math.log2(n)):
		if int(math.log2(n))%2:
			print ("Bob")
		else:
			print ("Alice")
	else:
		print ("Alice")