n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    if i%2!=0:
        break
    s+=i
print(s)
    