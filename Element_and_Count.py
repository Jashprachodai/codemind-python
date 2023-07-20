n=int(input())
ls=list(map(int,input().split()))
d={}
for i in ls:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d.keys():
    print(i,d[i],end=' ')
    