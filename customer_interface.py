#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import customer_details
import update_customer_details
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()	
if form.getvalue('get_data'):
	user=security.protect_data(form.getvalue('user'))
	get_data = security.protect_data(form.getvalue('get_data'))
	got_it=customer_details.get_any_value(user,get_data)
	print("%s"%got_it)
if form.getvalue('update_account_details'):
	username=security.protect_data(form.getvalue('update_account_details'))
	email = security.protect_data(form.getvalue('s_email'))
	contact = security.protect_data(form.getvalue('s_mobile'))
	fname = security.protect_data(form.getvalue('s_fname'))
	lname = security.protect_data(form.getvalue('s_lname'))
	middle_name = security.protect_data(form.getvalue('s_middlename'))
	flag_bit=update_customer_details.update_account_details(username,email,contact,fname,lname,middle_name)
	print("%s"%flag_bit)
	