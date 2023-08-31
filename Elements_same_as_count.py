n=int(input())
ls=list(map(int,input().split()))
d={}
for i in ls:
    if ls.count(i)==i:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
for i in d.keys():
    if d[i]==i:
        print(i,end=' ')
if len(d)==0:
    print(-1)
        
    