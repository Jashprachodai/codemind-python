n=int(input())
l=list(map(int,input().split()))
last=-1
for i in range(len(l)):
    if l[i]%2==0:
        last=l[i]
print(last)