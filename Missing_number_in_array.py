t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().split()))
    s=sum(ls)
    tot=(n*(n+1))//2
    print(tot-s)
        