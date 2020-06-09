import sys
ques=["?"]
for i in range(1,101):
	ques.append(i)
print (*ques)
sys.stdout.flush()
ans=[]
n=bin(int(input()))[2:]
n="0"*(14-len(n))+n
for i in range(7):
	ans.append(n[i])
ques=["?"]
for i in range(1,101):
	ques.append(i*128)
print (*ques)
sys.stdout.flush()
n=bin(int(input()))[2:]
n="0"*(14-len(n))+n
for i in range(7,14):
	ans.append(n[i])
answer="! "
answer=int(("".join(map(str,ans))),2)
print ("! "+str(answer))