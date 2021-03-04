import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	odd, even = [], []
	for i in a:
		if i%2:
			odd.append(i)
		else:
			even.append(i)
	odd.sort(reverse=True)
	even.sort(reverse=True)
	i, j = 0, 0
	turn = 1
	al, bo = 0, 0
	while i!=len(even) or j!=len(odd):
		if turn:
			if i==len(even):
				j += 1
			elif j==len(odd):
				al += even[i]
				i += 1
			elif even[i]>=odd[j]:
				al += even[i]
				i += 1
			else:
				j += 1
			turn = 0
		else:
			if i==len(even):
				bo += odd[j]
				j += 1
			elif j==len(odd):
				i += 1
			elif odd[j]>=even[i]:
				bo += odd[j]
				j += 1
			else:
				i += 1
			turn = 1
	if al>bo:
		print ("Alice")
	elif al==bo:
		print ("Tie")
	else:
		print ("Bob")




