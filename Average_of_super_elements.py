n=int(input())
ls=list(map(int,input().split()))
t=0
c=0
for i in ls:
    if i==ls.count(i):
        t+=i
        c+=1
        ls.remove(i)
if t==0:
    print(-1)
else:
    av=t/c
    print(f'{av:.2f}')