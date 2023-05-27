a=int(input())
s=list(map(int,input().split()))
b=int(input())
e=list(map(int,input().split()))
q=int(input())
c=0
for i in range(len(s)):
    if q>=s[i] and q<=e[i]:
        c+=1
print(c)