n=int(input())
l=list(map(int,input().split()))
n=[]
for i in l:
    if i not in n:
        n.append(i)
for x in n:
    print(x,end=' ')