n=int(input())
x=[0]*n
y=[0]*n
r=[0]*n
kibou=[0]*n
for i in range(n):
    kibou[i]=list(map(int,input().split()))

syutu=[0]*n

indices=[*range(n)]
sorted_indices=sorted(indices, key=lambda i: kibou[i][2])
sorted_num=[kibou[i] for i in sorted_indices]

for i in range(n):
    ima=sorted_num[sorted_indices[i]]
    syutu[sorted_indices[i]]=[sorted_num[i][0],sorted_num[i][1],sorted_num[i][0]+1,sorted_num[i][1]+1]
print('---------------------------')

for i in range(n):

    ima_i=sorted_num[i]
    dame=sorted_indices[i]

    x_min_l=float('inf')
    x_min_r=float('inf')
    y_min_l=float('inf')
    y_min_r=float('inf')
    for j in range(n):

        if(dame==sorted_indices[j]):
            pass
        else:


            ima_j=syutu[sorted_indices[j]]
            #左上 -1必要
            if(ima_j[2]<=ima_i[0] and ima_j[3]<=ima_i[1]):
                if(l_ue_max<(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])):
                    l_ue_max=(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])
                    l_ue_max_num=ima_j
                else:
                    pass



            elif(ima_j[0]<=ima_i[0] and ima_j[1]>=ima_i[1]):
                if(l_ue_max<(ima_i[0]-ima_j[0])*(ima_j[1]-ima_i[1])):
                    l_ue_max=(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])
                    l_ue_max_num=ima_j
                else:
                    pass
            elif(ima_j[0]<ima_i[0] and ima_j[1]<ima_i[1]):
                if(l_ue_max<(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])):
                    l_ue_max=(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])
                    l_ue_max_num=ima_j
                else:
                    pass
            elif(ima_j[0]<ima_i[0] and ima_j[1]<ima_i[1]):
                if(l_ue_max<(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])):
                    l_ue_max=(ima_i[0]-ima_j[0])*(ima_i[1]-ima_j[1])
                    l_ue_max_num=ima_j
                else:
                    pass
        #     else:
        #         # print(x_min_r)
        #         # print(ima_j[0])
        #         # print(ima_i[0])
        #         x_min_r=min(x_min_r,ima_j[0]-ima_i[0]-1)
        #
        #     if(ima_j[1]<ima_i[1]):
        #         y_min_l=min(y_min_l,ima_i[1]-ima_j[1]+1)
        #
        #     elif(ima_j[1]==ima_i[1]):
        #         y_min_l=0
        #         y_min_r=0
        #     else:
        #         y_min_r=min(y_min_r,ima_j[1]-ima_i[1]-1)
        #     if(sorted_indices[i]==16):
        #         print(i)
        #         input()
        #         print(j)
        #         print(syutu[j])
        #         print(x_min_l,x_min_r,y_min_l,y_min_r)
        #
        #     # print(j)
        #     # print(syutu[j])
        #     # print(x_min_l,x_min_r,y_min_l,y_min_r)
        # # if(i==12):
        # #     print(x_min_l,x_min_r,y_min_l,y_min_r)
    if(x_min_l==float('inf')):
        x_min_l=ima_i[0]-1
    if(x_min_r==float('inf')):
        x_min_r=10000-ima_i[0]
    if(y_min_l==float('inf')):
        y_min_l=ima_i[1]-1
    if(y_min_r==float('inf')):
        y_min_r=10000-ima_i[1]
    syutu[sorted_indices[i]]=[ima_i[0]-x_min_l,ima_i[1]-y_min_l,ima_i[0]+x_min_r,ima_i[1]+y_min_r]
    # print(i)
    # print(sorted_indices[i])
    # print(*syutu[sorted_indices[i]])
    # input()
for i in range(n):

    print(*syutu[i])
    # if(syutu[i][0]>=syutu[i][2]):
    #     input()
    # elif(syutu[i][1]>=syutu[i][3]):
    #     input()
