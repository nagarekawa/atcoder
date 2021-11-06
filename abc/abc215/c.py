s,k=map(str,input().split())
k=int(k)


import itertools
l=[0]*len(s)
for i in range(len(s)):
    l[i]=s[i]
p_list = list(set(itertools.permutations(l, len(s))))
p_list.sort()
# print(p_list)
print(*list(p_list[k-1]),sep='')


def find(fl):
    pass


find(1<<len(s))
print(1<<len(s))