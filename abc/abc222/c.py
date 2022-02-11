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




