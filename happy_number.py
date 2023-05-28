n=int(input())
def sq(n):
    s=0
    while n!=0:
        x=n%10
        s+=x*x
        n=n//10
    return s
while 1:
    n=sq(n)
    if n<10:
        break
print(n==1 or n==7)