n,m=map(int,input().split())
a=[0]*m
b=[0]*m
for i in range(m):
    a[i],b[i]=map(int,input().split())
lis=[[] for i in range(n)]
for i in range(m):
    lis[a[i]-1].append(b[i]-1)
    lis[b[i]-1].append(a[i]-1)
seen=[0]*n
ans=[0]*n
def dfs(start,hukasa):
    seen[start]=True
    for i in lis[start]:
        if(seen[i]==False):
            seen[i]=True
            print(i)
            if(i==n-1):
                ans[hukasa]=ans[hukasa]+1
            else:
                dfs(i,hukasa+1)
hukasa=0
print(lis)
dfs(0,hukasa)
print(ans)
print('----------')
for i in range(n):
    if(ans[i]!=0):
        print(ans[i])
        exit()
print(0)
