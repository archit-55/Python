#!/usr/bin/python3

import subprocess
q=input("enter:")
subprocess.call(["qrencode" , "-s" , "16*16" , "-o" , "qrc.png",q])
print(q)
