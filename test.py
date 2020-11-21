string=str(input().strip())
l=[]
for i in range(len(string)):
    if string[i] not in l:
        l.append(string[i])
min=9999
for i in range(len(string)):
    l2=[]+l[:]
    k=-1
    for j in range(i,len(string)):
        if string[j] in l2:
            l2.remove(string[j])
        if l2==[]:
            k=j
            break
    if k!=-1:
        temp=k-i
        if temp<min:
            min=temp
print(min+1)