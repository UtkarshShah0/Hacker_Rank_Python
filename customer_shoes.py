#N= int(input("Enter No. Of Shoes"))
#L=[]
#for i in range (0,N):
 #   a=int(input("Enter size"))
  #  L.append(a)
#a=int(input("Enter No. of Customers"))
#c=0
#for i in range(0,a+1):
#    b=int(input("Enter size"))

 #   if b in L:
  #        L.remove(b)
   #       c+=int(input("Enter Prize"))
#print(c)


N= int(input())
L=[]
for i in range (0,N):
    a=input().split()
    L.append(a)
c=0
for i in range(0,a):
    b,c=input().split()

    if b in L:
          L.remove(b)
          c+=c
print(c)
      
     
