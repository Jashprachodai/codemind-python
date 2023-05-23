n=int(input())
l=list(map(int,input().split()))
a=l[:n//2:]
b=l[n//2::]
b=b[::-1]
b.extend(a)
for i in b:
    print(i,end=' ')