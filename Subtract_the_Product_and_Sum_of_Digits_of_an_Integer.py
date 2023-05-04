n=int(input())
s=0
p=1
while n!=0:
    x=n%10
    s+=x
    p*=x
    n=n//10
print(abs(s-p))