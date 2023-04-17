r,c=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(r)]
es=0
os=0
for i in range(r):
    if i % 2 == 0:
            es+=sum(lst[i])
    else:
            os+=sum(lst[i])
print(es,os,end=' ')