def prime(n):
    if n==1:
        return False
    for i in range(2,1+int((n**0.5))):
        if n%i==0:
            return False
    return True
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0 and not prime(i):
        c+=1
print(c)
    