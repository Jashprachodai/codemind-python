def sq(n):
    a=n**0.5
    b=int(n**0.5)
    return a-b==0
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if sq(i):
        s+=i
print(s)
