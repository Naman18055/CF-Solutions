import math
for nt in range(int(input())):
	n = int(input())
	if math.log2(n)==int(math.log2(n)):
		print ("NO")
	else:
		print ("YES")