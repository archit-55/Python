#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,-11,400,6,0,9]
a=[]
b=[]

for i in adhoc:
    if(i>5):
        a.append(i)

    elif(i<=2):
        b.append(i)

else:


    print("Greater than 5:",a)
    print("less than equal to 2:",b)

