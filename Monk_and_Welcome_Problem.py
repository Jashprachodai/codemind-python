n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    a[i]=a[i]+b[i]
for x in a:
    print(x,end=' ')
    