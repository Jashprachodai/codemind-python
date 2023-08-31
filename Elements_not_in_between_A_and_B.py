n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
c=[i for i in range(a,b+1)]
s=0
t=0
for i in ls:
    if i not in c:
        t=1
        print(i,end=' ')
if t==0:
    print(-1)