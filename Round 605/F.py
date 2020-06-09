s=input()
t=input()
os,ot,cs,ct=0,0,0,0
for i in s:
	if i=="(":
		os+=1
	else:
		cs+=1
for i in t:
	if i=="(":
		ot+=1
	else:
		ct+=1
if os>ot:
	