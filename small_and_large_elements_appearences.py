s=input()
mx=max(s)
mn='z'
for i in s:
    if i!=' ':
        mn=min(mn,i)
print(mn,s.count(mn),mx,s.count(mx),end=' ')