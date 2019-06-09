#!/usr/bin/python3

import webbrowser
data=input("Search")
webbrowser.open_new('http://www.google.com/search?q='+data)
if data=='hello' :
    webbrowser.open_new_tab('http://www.google.com/search?q=wwe')
else:
    print("bye")
