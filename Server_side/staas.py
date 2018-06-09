#!/usr/bin/python3

import cgi
cgitb.enable()
import subprocess 

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

drive_name = web_data.getvalue('dn')
drive_size = web_data.getvalue('ds')

# creating thin lvm partition

subprocess.getoutput("sudo lvcreate --name " + drive_name + " -V"+drive_size+"M --thin cloud/pool1")

# now formatting the partiton 

subprocess.getoutput("sudo mkfs.xfs /dev/cloud/"+drive_name)

# mounting storage on server side first 

subprocess.getoutput("sudo mkdir /var/www/html/"+drive_name)

subprocess.getoutput("sudo mount /dev/cloud/"+drive_name "   /var/www/html/"+drive_name)

print("Everything is done") 
