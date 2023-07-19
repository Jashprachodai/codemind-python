n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if i==ls.count(i):
        c+=1
        ls.remove(i)
print(c)