#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

import os
import time
import socket

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

software = web_data.getvalue('software')
user = web_data.getvalue('user')

ip = socket.gethostbyname(socket.gethostname())

if software == 'firefox' :
	print("Plz wait firefox is about to start ... ")
	time.sleep(2)
	os.system('ssh  -l   '+user+ ' ' + ip +  '  -X  firefox') 
	
if software == 'gedit' :
	print("Plz wait gedit is about to start ... ")
	time.sleep(2)
	os.system('ssh  -l   '+user+ ' ' + ip + ' -X  gedit') 

if software == 'calculator':
	print("Plz wait calculator is about  to start ... ")
	time.sleep(2)
	os.system('ssh -l  '+ user + ' ' + ip + '  -X gnome-calculator')


