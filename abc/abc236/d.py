# ans=1
# # for i in range(1,16):
# #     ans=ans*i
# # print(ans)
# # import math
# # print(math.log(ans,10))
# n=8
# for i in range(0,n):
#     ans=ans*(2*n-1-(i*2))
#     print(ans)
# print(ans)
# import math
# print(math.log(ans,10))
n=int(input())
a=[[0 for i in range(2*n-1-j)] for j in range(2*n-1)]
print(a)

# a[0]=[1,1,1,1]
# print(a)
# a[0][1:]=[2,2,2]
# print(a)
# exit()
for i in range(2*n-1):
    a[i]=list(map(int,input().split()))
print(a)
