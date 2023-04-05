from collections import OrderedDict
a=input()
d=OrderedDict({})
for i in range(a):
    b=input()
    if b in d:
        d[b]+=1;

    else:
        d[b]=1;
print(len(d))#distinct words

for i in d:
    print(d[i],end=" ")
