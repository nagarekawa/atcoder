N=int(input())

a=list(map(int,input().split()))

A=int(input())

dp=[[False for i in range(A+1)] for i in range(N+1)]
dp[0][0]=True


for i in range(N):
    for j in range(A+1):
        dp[i+1][j]=dp[i][j]
        if(0<=j-a[i]):
            dp[i+1][j]=dp[i+1][j] or dp[i][j-a[i]]

if(dp[N][A]==True):
    print('YES')
else:
    print('NO')

print(dp)
