n=int(input())
ls=list(map(int,input().split()))
print(abs(sum(ls[0:(n//2)])-sum(ls[(n//2):])))