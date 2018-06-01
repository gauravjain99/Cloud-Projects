#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import mysql.connector as mysql 

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

email_id = web_data.getvalue('email')
password = web_data.getvalue('pass')

conn = mysql.connect(user='root',password='redhat',database='cloud',host='localhost')

'''if conn.is_connected():
        print("database connected successfully")
else:
        print("Something went wrong")
'''
cur = conn.cursor()

cur.execute("select * from registration where email='{}' and password='{}';".format(email_id,password))
data = cur.fetchall()

#print(data) 

if len(data) > 0:
	print("Entry done. You will be redirected soon ")
	print("<meta http-equiv='refresh' content='2;http://127.0.0.1/cloud/services.html'>")

elif len(data) == 0 :
	print("Email or Password is not correct")

else:
	print("Something is really wrong")
