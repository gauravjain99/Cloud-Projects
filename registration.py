#!/usr/bin/python3

import cgi 
import cgitb
cgitb.enable()
import mysql.connector as mysql 

print("Content-type:text/html")
print("")

web_data = cgi.FieldStorage()

username = web_data.getvalue('username')
name = web_data.getvalue('name')
email = web_data.getvalue('email')
password = web_data.getvalue('pass')

conn = mysql.connect(user="root",password="redhat",database="cloud",host="localhost")

'''if conn.is_connected():
	print("database connected successfully")
else:
	print("Something went wrong")
'''

cur = conn.cursor()

query = ("insert into registration (username,name,email,password) values('{}','{}','{}','{}');".format(username, name, email, password))

cur.execute(query)


conn.commit()
conn.close()

print("<h2>")
print("You have successfully registered")
print("</h2>")

print("Now please sign in to access the services")

 
