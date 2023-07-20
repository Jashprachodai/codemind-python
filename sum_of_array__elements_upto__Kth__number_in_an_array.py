n=int(input())
ls=list(map(int,input().split()))
k=int(input())
s=0
for i in ls:
    if k==0:
        break
    s+=i
    k-=1
print(s)
    