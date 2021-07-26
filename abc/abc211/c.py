
s=input()
le=len(s)
namae='chokudai'
dict_2={s:0 for s in namae}
dict_1={s:-1 for s in namae}
for i in range(len(s)):
    if(dict_2[s[-i-1]]==0):
        dict_2[s[-i-1]]=le-i-1
print(dict_2)
for i in range(len(s)):
    if(dict_1[s[i]]==-1):
        dict_1[s[i]]=i
print(dict_1)
print(len(dict_1))
# for i in range(len(dict)):
