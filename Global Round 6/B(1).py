t=int(input())
l=list(map(int,input().split()))
for i in l:
	if i%14>=1 and i%14<=6 and i>14:
		print ("YES")
	else:
		print ("NO")
	# if i%21==0:
	# 	print ("NO")
	# else:
	# 	n=(i//21)+1
	# 	if i<(n*21-(n-1)*7) and i>(n*21-(n-1)*7-7):
	# 		print ("YES")
	# 	else:
	# 		print ("NO")