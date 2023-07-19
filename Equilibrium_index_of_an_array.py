t=int(input())
for _ in range(t):
    s=int(input())
    ls=list(map(int,input().split()))
    for i in range(s):
        if sum(ls[0:i])==sum(ls[i+1:]):
            print(i)
            break
    else:
        print(-1)