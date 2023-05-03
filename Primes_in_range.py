a=int(input())
b=int(input())
def prime(n):
    if n==1:
        return False
    for x in range(2,int(1+n**0.5)):
        if n%x==0:
            return False
    return True  
c=0
for i in range(a,b+1):
    if prime(i):
        c+=1
print(c)