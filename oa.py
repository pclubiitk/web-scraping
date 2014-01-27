import urllib
import urllib2
for i in range(13000,13800):
	# Sending a get request to the URL
	html=urllib2.urlopen('http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt=%d&sbm=Y' %i)
	# Reading the response
	html=html.read()
	# Finding the name for a roll number
	beg=html.find('<b>Name: </b>')+len("<b>Name: </b>")
	# If no result found
	if(beg==-1):
		print "Something went wrong for roll No %d " %i
		continue
	end=html.find('</p>',beg)

	print "Roll No :" + str(i)
	print "Name : "+html[beg:end].strip()
	# Find the hostel info for the current roll number
	beg=html.find('<b>Hostel Info: </b>')+len("<b>Hostel Info: </b>")
	if(beg==-1):
		print "Roll No %d invalid" %i
		continue
	end=html.find('<br>',beg)
	print "Address : "+html[beg:end].strip()+"\n\n"
