#!/usr/bin/python 
import cgi, cgitb 
import sys
import security
import admin_show_customers
import no_found
import customer_details
print("Content-type:text/html;Content-type: image/jpeg\r\n\r\n")
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()	
if form.getvalue('flag'):
	flag=form.getvalue("flag")
	info=no_found.no_found("No new requests")
	if flag=="approved_customers":
		info=admin_show_customers.show_customers(1)
	elif flag=="rejected_customers":
		info=admin_show_customers.show_customers(-1)
	else:
		info=admin_show_customers.show_customers(0)
	print("%s"%info)
if form.getvalue('get_data'):
	user=security.protect_data(form.getvalue('user'))
	get_data = security.protect_data(form.getvalue('get_data'))
	got_it=customer_details.get_any_value(user,get_data)
	print("%s"%got_it)
if form.getvalue('get_data_id') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	get_data_id=security.protect_data(form.getvalue('get_data_id'))
	got_it=customer_details.get_any_value_by_id(userid,get_data_id)
	print("%s"%got_it)
if form.getvalue('get_document') and form.getvalue('userid'):
	userid = security.protect_data(form.getvalue('userid'))
	username=customer_details.get_any_value_by_id(userid,"username")
	get_document=security.protect_data(form.getvalue('get_document'))
	got_it=customer_details.get_any_document(username,get_document)
	print("%s"%got_it)