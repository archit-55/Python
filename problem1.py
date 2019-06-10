#!/usr/bin/python3

import datetime
name=input("Enter name:")
age=int(input("enter age:"))
print("Name:",name)
print("Age:",age)

x=95-age
current_year=datetime.datetime.now()
print("You will turn 95 in the year" ,x+current_year.year)



