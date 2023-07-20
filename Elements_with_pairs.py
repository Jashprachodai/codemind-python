n=int(input())
ls=list(map(int,input().split()))
for i in ls:
    print(i,end=' ')
if n%2!=0:
    print(0)
    