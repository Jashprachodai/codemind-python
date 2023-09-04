def pali(s):
    s=s.lower()
    return s=="".join(list(reversed(s)))
n = input()
l = n.split(" ")
c=0
for i in l:
    if pali(i):
        c+=1
print(c)