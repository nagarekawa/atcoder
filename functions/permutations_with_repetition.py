#重複順列
#aからbまでのm個の数字の中からn個を選ぶ
a,b,m,n=map(int,input().split())
permutation=[0]*3
def dfs(minn,maxx,size,depth):
    if(depth==size):
        print(*permutation,sep='')
    else:
        for i in range(max-min+1):
            permutation[depth]=minn+i
            depth=depth+1
            dfs(minn,maxx,size,depth)

dfs(a,b,n,0)