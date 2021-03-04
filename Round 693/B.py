import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	one = a.count(1)
	two = a.count(2)
	if two%2==0:
		if one%2==0:
			print ("YES")
		else:
			print ("NO")
	else:
		if one!=0 and one%2==0:
			print ("YES")
		else:
			print ("NO")

