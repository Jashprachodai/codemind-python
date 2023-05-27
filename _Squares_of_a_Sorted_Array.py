n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    x=l[i]
    x=x*x
    l[i]=x
l.sort()
for x in l:
    print(x,end=' ')
    