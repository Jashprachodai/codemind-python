n=int(input())
ls=list(map(int,input().split()))
nl=[]
for i in ls:
    if i not in nl:
        nl.append(i)
for i in nl:
    print(i,end=' ')