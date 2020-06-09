c=input()
l=input().split()
x=0
for i in l:
	if c[0]==i[0] or c[1]==i[1]:
		print ("YES")
		x=1
		break
if x!=1:
	print ("NO")