def prime(n):
    if n==1:
        return False
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            return False
    return True
def rev(n):
    r=0
    while n!=0:
        x=n%10
        r=(r*10)+x
        n=n//10
    return r
n=int(input())
r=rev(n)
if prime(n) and prime(r):
    print('circular prime')
elif prime(n):
    print('prime but not a circular prime')
else:
    print('not prime')
