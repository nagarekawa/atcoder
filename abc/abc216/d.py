n=int(input())
ans=[]
while(1):
    if(n==0):
        break
    if(n%2==0):
        n=n//2
        ans.append('B')
    else:
        n=n-1
        ans.append('A')

ans.reverse()
print(''.join(ans))
