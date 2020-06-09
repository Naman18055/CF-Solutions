a,b,c,d=map(int,input().split())
if a>b and (c>0 or d>0):
	print ("NO")
	exit()
if d>c and (a>0 or b>0):
	print ("NO")
	exit()
if a==b+1 and (c==0 and d==0):
	print ("YES")
	for i in range(a+b):
		if i%2==0:
			print (0,end=" ")
		else:
			print (1,end=" ")
	print ()
	exit()
if d==c+1 and (a==0 or b==0):
	print ("YES")
	for i in range(c+d):
		if i%2==0:
			print (3,end=" ")
		else:
			print (2,end=" ")
	print ()
	exit()
onerem=b-a+1
tworem=c-d+1
if onerem==tworem:
	# if a==0:
	# 	print ("YES")
	# 	for i in range(2*b):
	# 		if i%2==0:
	# 			print (1,end=" ")
	# 		else:
	# 			print (2,end=" ")
	# 	print ()
	# 	exit()
	print ("YES")
	for i in range(2*a):
		if i%2==0:
			print (0,end=" ")
		else:
			print (1,end=" ")
	for i in range(2*(b-a)):
		if i%2==0:
			print (2,end=" ")
		else:
			print (1,end=" ")
	for i in range(2*d):
		if i%2==0:
			print (2,end=" ")
		else:
			print (3,end=" ")
	print ()
	exit()
elif abs(onerem-tworem)==1:
	
	if onerem>tworem:
		if a==0:
			print ("YES")
			for i in range(2*c+1):
				if i%2==0:
					print (1,end=" ")
				else:
					print (2,end=" ")
			print ()
			exit()
		print ("YES")
		for i in range(2*a):
			if i%2==0:
				print (1,end=" ")
			else:
				print (0,end=" ")
		for i in range(2*(b-a)):
			if i%2==0:
				print (1,end=" ")
			else:
				print (2,end=" ")
		for i in range(2*d-1):
			if i%2==0:
				print (3,end=" ")
			else:
				print (2,end=" ")
		print ()
		exit()
	else:
		if a==0:
			print ("YES")
			for i in range(2*b+1):
				if i%2==0:
					print (2,end=" ")
				else:
					print (,end=" ")
			print ()
			exit()
		for i in range(2*a):
			if i%2==0:
				print (0,end=" ")
			else:
				print (1,end=" ")
		for i in range(2*(b-a)):
			if i%2==0:
				print (2,end=" ")
			else:
				print (1,end=" ")
		for i in range(2*d+1):
			if i%2==0:
				print (2,end=" ")
			else:
				print (3,end=" ")
		print ()
		exit()
else:
	print ("NO")
