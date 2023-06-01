def prime(n):
    if n==1:
        return False
    for i in range(2,1+int((n**0.5))):
        if n%i==0:
            return False
    return True
def pal(n):
    return str(n)== "".join(reversed(str(n)))
a=int(input())
while 1:
    a+=1
    if prime(a) and pal(a):
        print(a)
        break