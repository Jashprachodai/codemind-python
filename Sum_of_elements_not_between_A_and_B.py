n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())
c=[i for i in range(a,b+1)]
s=0
for i in ls:
    if i not in c:
        s+=i
print(s)