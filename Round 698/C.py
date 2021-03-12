import math
def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    count={}
    for i in arr:
        count[i]=count.get(i,0)+1
    for i in count:
        if(count[i]!=2):
            return 'NO'
    sum=0;
    for i in sorted(set(arr),reverse=True):
        if (i-sum)>0 and (i-sum)%(n*2)==0:
            sum+=(i-sum)//n
        else:
            return 'NO'
        n-=1
    return 'YES'


for _ in range(int(input())):
    print(solve())