#!/usr/bin/python
import config
import customer_details
import no_found
def show_customers(bit):
	conn,cursor=config.connect_to_database()
	sql="select * from customers where hasAcc='%s'"%bit
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		row_num=cursor.rowcount
		bit=int(bit)
		if bit==0:
			flag="New customers"
		elif bit==1:
			flag="Approved customers"
		elif bit==-1:
			flag="Rejected customers"
		else:
			flag="New customers"
		if int(row_num)==0:
			cust=no_found.no_found("No "+flag)
		else:
			cust="""<div class="row" style="margin:20px;"><caption><h3>%s</h3></caption><table class="customerTable table-striped"><tr><td align="left">Index no.</td><td align="left">Username</td><td align="left">Full Name</td><td align="left">Email</td><td align="left">Contact no.</td></tr>"""%(flag)
			i=1
			for row in results:
				cid="userid"+str(row[0])
				username=row[1]
				fname=row[2].capitalize()
				lname=row[3].capitalize()
				middle_name=row[12].capitalize()
				email=row[4]
				contact=row[6]
				full_name="%s %s %s"%(fname,middle_name,lname)
				cust+="""<div id='%s'><tr><td align="left">%s</td><td align="left">%s</td><td align="left">%s</td><td align="left">%s</td><td align="left">%s</td></tr></div>"""%(cid,i,username,full_name,email,contact)
				i+=1
			cust+="</table></div>"
		return cust
	except:
		return "-1"