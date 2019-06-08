#!/usr/bin/python3

l=[]
a=int(input("no. of inputs:"))
for i in range(0,a) :
    b=int(input("enter no."))
    l.append(b)
print(l) 

c=int(input("enter no.:"))
if c in l:
    l.remove(c)
else:
    print("not found")
print("list=",l)    
    
