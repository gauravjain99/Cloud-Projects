#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

provide_service = web_data.getvalue('provide_service')

if provide_service == 'IAAS' :
	print("You have chosen IAAS.\n Great, enjoy Cloud Infrastructure Service ")
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/iaas.html'>")

if provide_service == 'SAAS' :
	print("You have chosen SAAS.\n Great, enjoy Cloud Software Service ")
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/saas.html'>")

if provide_service == 'STAAS' :
	print("You have chosen STAAS.\n Great, enjoy Cloud Storage Service ")
	print("<meta http-equiv='refresh' content='1;http://192.168.122.64/staas.html'>")

if provide_service == 'PAAS' :
	print("You have chosen PAAS.\n Great, enjoy Cloud Platform Service ")
	print("<meta http-equiv='refresh' content='1;http://127.0.0.1/cloud/paas.html'>")
