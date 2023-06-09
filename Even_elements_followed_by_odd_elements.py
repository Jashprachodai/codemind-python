n=int(input())
l=list(map(int,input().split()))
a=[i for i in l if i%2==0]
b=[i for i in l if i%2!=0]
a.extend(b)
for i in a:
    print(i,end=' ')