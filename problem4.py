#!/usr/bin/python3

import os
import string

username=input("Enter username:")
flag=0

for i in list(username):
    if i not in string.ascii_letters :
        print("Incorrect Username!")
        flag=1   
if flag==0 :
    os.system('sudo useradd'+username)
    os.system('sudo passwd'+username)


