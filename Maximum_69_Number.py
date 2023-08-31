def six(n,p):
    n=str(n)
    n=[*n]
    if n[p-1]=='6':
        n[p-1]='9'
    else:
        n[p-1]='6'
    return int("".join(n))
n=int(input())
ls=[]
ls.append(n)
for i in range(1,len(str(n))+1):
    ls.append(six(n,i))
print(max(ls))