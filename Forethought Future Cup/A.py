s=input()
count=0
for i in s:
	if i=="a":
		count+=1
maxlength = count*2-1
print (min(maxlength,len(s)))