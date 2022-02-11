n,m=map(int,input().split())
a=[0 for i in range(4)]
for i in range(4):
    a[i]=input()
print(a)

pea=[-1 for i in range(2*n)]
for i in range(2*n):
    if(i%2==0):
        pea[i]=i+1
print(pea)
def kekka(iti,ni):
    if(iti=='G' and ni=='C'):
        return 1
    elif(iti=='G' and ni=='P'):
        return 2
    elif(iti=='G' and ni=='G'):
        return 3
    elif(iti=='C' and ni=='C'):
        return 3
    elif(iti=='C' and ni=='P'):
        return 1
    elif(iti=='C' and ni=='G'):
        return 2
    elif(iti=='P' and ni=='C'):
        return 2
    elif(iti=='P' and ni=='P'):
        return 3
    elif(iti=='P' and ni=='G'):
        return 1
ans=[0 for i in range(2*n)]
for i in range(m):
    for j in range(2*n):
        if(pea[j]!=-1):
            iti=a[j][i]
            ni=a[pea[j]][i]
            kotae=kekka(iti,ni)
            if(kotae==1):
                ans[j]=ans[j]+1
            elif(kotae==2):
                ans[pea[j]]=ans[pea[j]]+1
            else:
                pass
    



