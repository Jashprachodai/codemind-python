n=int(input())
ls=list(map(int,input().split()))
for i in range(n//2):
    print(ls[i],ls[n-i-1],end=' ')
if n%2!=0:
    print(ls[(n//2)],0,end=' ')