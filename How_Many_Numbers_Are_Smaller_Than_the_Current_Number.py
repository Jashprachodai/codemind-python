n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    c=0
    for j in l:
        if i>j:
            c+=1
    e.append(c)
for x in e:
    print(x,end=' ')