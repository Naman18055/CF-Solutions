import sys
def div(n) : 
	i = 1
	temp=[]
	while i <= n : 
		if (n % i==0) : 
			temp.append(i) 
		i = i + 1
	return temp

l=[4,8,15,16,23,42]
print ("?",1,2)
sys.stdout.flush()
a=int(input())
d=div(a)
canbe=[]
for i in d:
	if i in l:
		if (a//i) in l:
			canbe.append(i)
			canbe.append(a//i)
			break
print ("?",1,3)
sys.stdout.flush()
b=int(input())
d=div(b)
sure=[]
for i in d:
	if i in l:
		if (b//i) in l:
			sure.append(i)
			sure.append(b//i)
			break
for i in range(2):
	if canbe[i] in sure:
		one=canbe[i]
		two=canbe[1-i]
		three=b//one
print ("?",4,5)
sys.stdout.flush()
c=int(input())
d=div(c)
canbe=[]
for i in d:
	if i in l:
		if (c//i) in l:
			canbe.append(i)
			canbe.append(c//i)
			break
print ("?",4,6)
sys.stdout.flush()
e=int(input())
d=div(e)
sure=[]
for i in d:
	if i in l:
		if (e//i) in l:
			sure.append(i)
			sure.append(e//i)
			break
for i in range(2):
	if canbe[i] in sure:
		four=canbe[i]
		five=canbe[1-i]
		six=e//four
print ("!",one,two,three,four,five,six)

