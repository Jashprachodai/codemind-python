n=int(input())
ls=list(map(int,input().split()))
print(abs(sum(ls[0::2])-sum(ls[1::2])))