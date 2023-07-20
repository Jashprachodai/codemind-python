n=int(input())
ls=list(map(int,input().split()))
print(sum(ls[0:(n//2)]))
print(sum(ls[(n//2):]))