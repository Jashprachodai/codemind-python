n=int(input())
ls=list(map(int,input().split()))
nl=[]
for i in ls:
    if ls.count(i)==i and i not in nl:
        nl.append(i)
if len(nl)>=1:
    print(min(nl),max(nl),end=' ')
else:
    print(-1)
        
    