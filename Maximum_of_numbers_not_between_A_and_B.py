n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
c=[i for i in range(a,b+1)]
m=-1
t=0
for i in ls:
    if i not in c:
        t=1
        m=max(m,i)
if t==0:
    print(-1)
else:
    print(m)