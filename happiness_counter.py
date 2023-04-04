# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=input().split()
#a no. of array //b no. of in set
array=list(map(int,input().split())) 
happiness=0
sad=0
 

d=set(map(int,input().split()))
for i in array:
    if i in d:
        happiness+=1
    
e=set(map(int,input().split()))
for i in array:
    if i in e:
        sad+=1
   
    
print(happiness-sad)
    
