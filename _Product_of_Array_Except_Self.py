n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(n):
    p=1
    for j in range(n):
        if l[j]!=l[i]:
            p*=l[j]
    x.append(p)
for i in x:
    print(i,end=' ')