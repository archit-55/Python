#!/usr/bin/python3

import time
import subprocess
import webbrowser
import os

option='''
press 1 for vlc
press 2 for date and time
press 3 to search on google
press 4 to search on youtube
press 5 to reboot system
'''
print(option)

choice=input()

if choice == '1' :
	subprocess.getoutput("vlc")
elif choice== '2' :
	current_time=time.ctime()
	print(current_time)
elif choice =='3' :
	data=input("Search here:")
	webbrowser.open_new_tab('http://www.google.com/search?q='+data)
elif choice =='4' :
	video=input("enter here:")
	webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+video)
elif choce==5:
	os.system("sudo reboot -f")
else:
	print("error:Invalid option")
	
