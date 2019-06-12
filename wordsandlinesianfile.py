#!/usr/bin/python3

file_name=input("Enter filename:")
f=open(file_name)
data=f.read()
words=len(data.split())
num_lines=len(data.splitlines())
print("no of words=",words)
print("no. of lines:",num_lines)
