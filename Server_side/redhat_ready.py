#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import subprocess
import socket

ip = socket.gethostbyname(socket.gethostname())

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

ram = web_data.getvalue('or')
cpu = web_data.getvalue('oc')
hdd = web_data.getvalue('oh')


subprocess.getoutput("sudo virt-install --name redhatclient2 --ram "+ram +" --vcpu "+cpu+" --disk path=/var/lib/libvirt/images/virt_redhat1.qcow2 --import --noautoconsole --graphics vnc,listen=0.0.0.0,port=5980")

'''subprocess.getoutput("websockify --web=/usr/share/novnc 6080 "+ip+":5929 & > /dev/null") 

print("\nNow you will be redirected to your selected Virtual Machine\n")
print("<meta http-equiv='refresh' content='1;http://127.0.0.1:6080'>") 

'''
