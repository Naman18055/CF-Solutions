t=int(input())
for nt in range(t):
	n=int(input())
	d={"00":[],"01":[],"10":[],"11":[]}
	order={}
	alld={}
	for i in range(n):
		s=input()
		alld[s]=0
		order[s]=i
		if s[0]=="0" and s[-1]=="0":
			d["00"]=["00"]
		elif s[0]=="1" and s[-1]=="1":
			d["11"]=["11"]
		elif s[0]=="1" and s[-1]=="0":
			d["10"].append(s)
		else:
			d["01"].append(s)
	if len(d["00"])>0 and len(d["11"])>0 and len(d["10"])==0 and len(d["01"])==0:
		print (-1)
		continue
	elif len(d["01"])==len(d["10"]):
		print (0)
		print ()
		continue
	elif len(d["01"])>len(d["10"]):
		rr = (len(d["01"])-len(d["10"]))//2
		rev = []
		for i in d["01"]:
			reverse = i[::-1]
			if reverse not in alld:
				rev.append(i)
			if len(rev)>=rr:
				break
		if len(rev)>=rr:
			print (rr)
			for i in range(rr):
				print (order[rev[i]]+1,end=" ")
			print ()
		else:
			print (-1)
	else:
		rr = (len(d["10"])-len(d["01"]))//2
		rev = []
		for i in d["10"]:
			reverse = i[::-1]
			if reverse not in alld:
				rev.append(i)
			if len(rev)>=rr:
				break
		if len(rev)>=rr:
			print (rr)
			for i in range(rr):
				print (order[rev[i]]+1,end=" ")
			print ()
		else:
			print (-1)
	



