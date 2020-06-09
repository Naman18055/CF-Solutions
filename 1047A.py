x=int(input())
"""if x%3==0 and ((x/3)%3)==0:
	print (int(x/3)-1 , int(x/3)+1 , int(x/3)+1)
elif x%3==0:
	print (int(x/3) , int(x/3) , int(x/3))
elif x%3==1 and ((x-1)/3)%3==0:
	print (x//3-1,x//3+1,x//3+1)
elif x%3==1:
	print (x//3 , x//3 , x//3+1)
elif x%3==2 and ((x-2)/3)%3==0:
	print (x//3-2,x//3+2 , x//3+2)
else:
	print (x//3 , x//3+1 , x//3+1)"""
y=x//3
if x%3==0 and y%3==0:
	print (y-1,y-1,y+2)
elif x%3==0 and y%3!=0:
	print (y,y,y)
if y%3==0 and x%3!=0:
	if 3*y+1==x:
		print (y-1,y+1,y+1)
	else:
		print (y-1,y+1,y+2)
elif y%3==1 and x%3!=0:
	if 3*y+1==x:
		print (y,y,y+1)
	else:
		print (y,y+1,y+1)
elif y%3==2 and x%3!=0:
	if 3*y+1==x:
		print (y-1,y,y+2)
	else:
		print (y,y,y+2)