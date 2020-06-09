file = open("test.txt","w")
file.writelines("100000 5 \n")
for i in range(99999):
	file.writelines(str(i+1)+" "+str(i+2)+"\n")
