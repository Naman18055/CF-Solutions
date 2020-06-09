n,q=map(int,input().split())
d={}
ans=[]
blocked={}
for i in range(q):
	r,c=map(int,input().split())
	if (r,c) in d:
		if d[(r,c)]==False:
			d[(r,c)]=True
			if ans[-1]=="Yes":
				flag=False
				if r==1:
					if (r+1,c) in d:
						if d[(r+1,c)]==True:
							flag=True
							blocked[(r,c,r+1,c)]=1
							blocked[(r+1,c,r,c)]=1
					if (r+1,c-1) in d:
						if d[(r+1,c-1)]==True:
							flag=True
							blocked[(r,c,r+1,c-1)]=1
							blocked[(r+1,c-1,r,c)]=1
					if (r+1,c+1) in d:
						if d[(r+1,c+1)]==True:
							flag=True
							blocked[(r,c,r+1,c+1)]=1
							blocked[(r+1,c+1,r,c)]=1
				else:
					if (r-1,c) in d:
						if d[(r-1,c)]==True:
							flag=True
							blocked[(r,c,r-1,c)]=1
							blocked[(r-1,c,r,c)]=1
					if (r-1,c-1) in d:
						if d[(r-1,c-1)]==True:
							flag=True
							blocked[(r,c,r-1,c-1)]=1
							blocked[(r-1,c-1,r,c)]=1
					if (r-1,c+1) in d:
						if d[(r-1,c+1)]==True:
							flag=True
							blocked[(r,c,r-1,c+1)]=1
							blocked[(r-1,c+1,r,c)]=1
				if flag:
					ans.append("No")
				else:
					ans.append("Yes")
			else:
				ans.append("No")
				if r==1:
					if (r+1,c) in d:
						if d[(r+1,c)]==True:
							blocked[(r,c,r+1,c)]=1
							blocked[(r+1,c,r,c)]=1
					if (r+1,c-1) in d:
						if d[(r+1,c-1)]==True:
							blocked[(r,c,r+1,c-1)]=1
							blocked[(r+1,c-1,r,c)]=1
					if (r+1,c+1) in d:
						if d[(r+1,c+1)]==True:
							blocked[(r,c,r+1,c+1)]=1
							blocked[(r+1,c+1,r,c)]=1
				else:
					if (r-1,c) in d:
						if d[(r-1,c)]==True:
							blocked[(r,c,r-1,c)]=1
							blocked[(r-1,c,r,c)]=1
					if (r-1,c-1) in d:
						if d[(r-1,c-1)]==True:
							blocked[(r,c,r-1,c-1)]=1
							blocked[(r-1,c-1,r,c)]=1
					if (r-1,c+1) in d:
						if d[(r-1,c+1)]==True:
							blocked[(r,c,r-1,c+1)]=1
							blocked[(r-1,c+1,r,c)]=1
		else:
			d[(r,c)]=False
			if ans[-1]=="Yes":
				ans.append("Yes")
				if r==1:
					if (r,c,r+1,c) in blocked:
						del blocked[(r,c,r+1,c)]
						del blocked[(r+1,c,r,c)]
					if (r,c,r+1,c-1) in blocked:
						del blocked[(r,c,r+1,c-1)]
						del blocked[(r+1,c-1,r,c)]
					if (r,c,r+1,c+1) in blocked:
						del blocked[(r,c,r+1,c+1)]
						del blocked[(r+1,c+1,r,c)]
				else:
					if (r,c,r-1,c) in blocked:
						del blocked[(r,c,r-1,c)]
						del blocked[(r-1,c,r,c)]
					if (r,c,r-1,c-1) in blocked:
						del blocked[(r,c,r-1,c-1)]
						del blocked[(r-1,c-1,r,c)]
					if (r,c,r-1,c+1) in blocked:
						del blocked[(r,c,r-1,c+1)]
						del blocked[(r-1,c+1,r,c)]
			else:
				if r==1:
					if (r,c,r+1,c) in blocked:
						del blocked[(r,c,r+1,c)]
						del blocked[(r+1,c,r,c)]
					if (r,c,r+1,c-1) in blocked:
						del blocked[(r,c,r+1,c-1)]
						del blocked[(r+1,c-1,r,c)]
					if (r,c,r+1,c+1) in blocked:
						del blocked[(r,c,r+1,c+1)]
						del blocked[(r+1,c+1,r,c)]
				else:
					if (r,c,r-1,c) in blocked:
						del blocked[(r,c,r-1,c)]
						del blocked[(r-1,c,r,c)]
					if (r,c,r-1,c-1) in blocked:
						del blocked[(r,c,r-1,c-1)]
						del blocked[(r-1,c-1,r,c)]
					if (r,c,r-1,c+1) in blocked:
						del blocked[(r,c,r-1,c+1)]
						del blocked[(r-1,c+1,r,c)]
				if len(blocked)==0:
					ans.append("Yes")
				else:
					ans.append("No")
	else:
		d[(r,c)]=True
		if len(ans)==0:
			ans.append("Yes")
			continue
		else:
			if ans[-1]=="Yes":
				flag=False
				if r==1:
					if (r+1,c) in d:
						if d[(r+1,c)]==True:
							flag=True
							blocked[(r,c,r+1,c)]=1
							blocked[(r+1,c,r,c)]=1
					if (r+1,c-1) in d:
						if d[(r+1,c-1)]==True:
							flag=True
							blocked[(r,c,r+1,c-1)]=1
							blocked[(r+1,c-1,r,c)]=1
					if (r+1,c+1) in d:
						if d[(r+1,c+1)]==True:
							flag=True
							blocked[(r,c,r+1,c+1)]=1
							blocked[(r+1,c+1,r,c)]=1
				else:
					if (r-1,c) in d:
						if d[(r-1,c)]==True:
							flag=True
							blocked[(r,c,r-1,c)]=1
							blocked[(r-1,c,r,c)]=1
					if (r-1,c-1) in d:
						if d[(r-1,c-1)]==True:
							flag=True
							blocked[(r,c,r-1,c-1)]=1
							blocked[(r-1,c-1,r,c)]=1
					if (r-1,c+1) in d:
						if d[(r-1,c+1)]==True:
							flag=True
							blocked[(r,c,r-1,c+1)]=1
							blocked[(r-1,c+1,r,c)]=1
				if flag:
					ans.append("No")
				else:
					ans.append("Yes")
			else:
				ans.append("No")
				if r==1:
					if (r+1,c) in d:
						if d[(r+1,c)]==True:
							blocked[(r,c,r+1,c)]=1
							blocked[(r+1,c,r,c)]=1
					if (r+1,c-1) in d:
						if d[(r+1,c-1)]==True:
							blocked[(r,c,r+1,c-1)]=1
							blocked[(r+1,c-1,r,c)]=1
					if (r+1,c+1) in d:
						if d[(r+1,c+1)]==True:
							blocked[(r,c,r+1,c+1)]=1
							blocked[(r+1,c+1,r,c)]=1
				else:
					if (r-1,c) in d:
						if d[(r-1,c)]==True:
							blocked[(r,c,r-1,c)]=1
							blocked[(r-1,c,r,c)]=1
					if (r-1,c-1) in d:
						if d[(r-1,c-1)]==True:
							blocked[(r,c,r-1,c-1)]=1
							blocked[(r-1,c-1,r,c)]=1
					if (r-1,c+1) in d:
						if d[(r-1,c+1)]==True:
							blocked[(r,c,r-1,c+1)]=1
							blocked[(r-1,c+1,r,c)]=1
for i in ans:
	print (i)






