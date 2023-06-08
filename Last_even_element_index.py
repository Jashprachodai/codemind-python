n=int(input())
l=list(map(int,input().split()))
ind=-1
for i in range(len(l)):
    if l[i]%2==0:
        ind=i
print(ind)