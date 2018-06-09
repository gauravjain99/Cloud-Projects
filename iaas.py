#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import subprocess

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

os = web_data.getvalue("os")

if os == "redhat" :
	data = subprocess.getoutput("sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/virt_redhat3.qcow2")
	print(data)
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/iaas_redhat_require.html'>")






	
