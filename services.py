#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

servicetype = web_data.getvalue('service')

if servicetype == 'Private':
	print("Great you have chosen Private cloud, Soon you will be redirected to use Private CLoud Services")
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/services_private.html'>")
elif servicetype == 'Public' :
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/services_public.html'>")


