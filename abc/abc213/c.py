h,w,n=map(int,input().split())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())

yoko=[]
tate=[]
for i in range(n):
    yoko.append(a[i])
    tate.append(b[i])
yoko=sorted(list(set(yoko)))
tate=sorted(list(set(tate)))

for i in range(len(yoko)):
    for j in range(len(tate)):
        print(i,j)
