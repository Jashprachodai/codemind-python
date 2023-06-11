n=int(input())
ls=list(map(int,input().split()))
av=sum(ls)//len(ls)
c=0
for i in ls:
    if i >= av:
        c+=1
print(c)