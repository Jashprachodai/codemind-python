n=int(input())
ls=list(map(int,input().split()))
for i in ls:
    if i%2!=0:
        print(False)
        break
else:
    print(True)