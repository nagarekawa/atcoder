a,b,k=map(int,input().split())

import math

ans=''
a_da=0
b_da=0
for i in range(a+b):

    saidai=int(math.factorial(a+b-i)/(math.factorial(a-a_da)*(math.factorial(b-b_da))))
    print(saidai)
    if(k<saidai):
        k=k-saidai
        ans=ans+'b'
        b_da=b_da+1
    else:
        ans=ans+'a'
        a_da=a_da+1
    print(ans)
print(ans)
