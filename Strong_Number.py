import math
n=int(input())
t=n
f=0
while n!=0:
    x=n%10
    f+=math.factorial(x)
    n=n//10
if t==f:
    print(f"The number {t} is a strong number")
else:
    print(f"The number {t} is not a strong number")