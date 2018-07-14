import pymysql
import cgi, cgitb 
import sys
import os
import re
import private_data
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText

class Mail:
	USERNAME = private_data.admin_email
	PASSWORD = private_data.admin_passsword
	def send_mail(self,email_ad,mob,name):
		SMTPserver = 'smtp.gmail.com'
		sender =     private_data.admin_email
		destination = email_ad
		text_subtype = 'html'
		content="""\
		<b>Welcome to the Jon Snow (The Assistant)</b> <br> \
		dear %s ,<br> \
			You have registered your email address successfully <br> \
			Your Mobile number %s <br> \
		""" % (name,mob)
		subject="Sign up successfully"
		try:
			msg = MIMEText(content, text_subtype)
			msg['Subject']= subject
			msg['From']   = sender 
			conn = SMTP(SMTPserver)
			conn.set_debuglevel(False)
			conn.login(self.USERNAME, self.PASSWORD)
			try:
				conn.sendmail(sender, destination, msg.as_string())
			finally:
				conn.quit()
		except Exception:
			print("0")

m=Mail()
form = cgi.FieldStorage()
db=pymysql.connect("localhost",'root','','minor_Project')
print("Content-type:text/html\r\n\r\n")

if form.getvalue('s_email'):
	email = form.getvalue('s_email')
if form.getvalue('s_user'):
	user = form.getvalue('s_user')
if form.getvalue('s_mobile'):
	phone = form.getvalue('s_mobile')
if form.getvalue('s_password'):
	password = form.getvalue('s_password')
if form.getvalue('s_fname'):
	fname = form.getvalue('s_fname')
if form.getvalue('s_lname'):
	lname = form.getvalue('s_lname')
if form.getvalue('s_middlename'):
	middlename = form.getvalue('s_middlename')
if form.getvalue('s_gender'):
	gender = form.getvalue('s_gender')
if form.getvalue('s_dob'):
	dob = form.getvalue('s_dob')
if form.getvalue('s_postaladd'):
	postal_add = form.getvalue('s_postaladd')
if form.getvalue('s_permadd'):
	perm_add = form.getvalue('s_permadd')
if form.getvalue('s_pincode'):
	pincode = form.getvalue('s_pincode')
if form.getvalue('s_city'):
	city = form.getvalue('s_city')
if form.getvalue('s_state'):
	state = form.getvalue('s_state')
if form.getvalue('s_country'):
	country = form.getvalue('s_country')
cursor=db.cursor();
sql="INSERT INTO Candidates (username,fname,lname,middle_name,email,contact,password,dob,gender,postal_add,perm_add,pincode,city,state,country) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (user,fname,lname,middlename,email,phone,password,dob,gender,postal_add,perm_add,pincode,city,state,country)
try:
	cursor.execute(sql)
	db.commit()
	m.send_mail(email,phone,user)
	print("1")
except:
	db.rollback()
	print("0")
	
db.close()