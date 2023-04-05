n,a=map(int,input().split())
d=0
for i in range(n):
    c=list(map(int,input().split()))
    d+=((max(c))**2)
print(d%a)
