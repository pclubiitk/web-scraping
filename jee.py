import urllib
import urllib2
# Range of roll numbers to extract data for
for i in range(6006070,6006370):
	# Setting up post params
	values={'regno':i,'submit':'Submit'}
	# sending request to the server
	html=urllib2.urlopen('http://www.iitkgp.ernet.in/jee/resultstatus.php',urllib.urlencode(values))
	html=html.read()
	# Finding the name of the student
	beg=html.find('Name  :')
	if(beg==-1):
		print "Roll No %d not selected" %i
		continue
	end=html.find('<br>',beg)
	print "Roll No :" + str(i)
	print "Name : "+html[beg+8:end]
	# Searching for persons rank
	beg= html.find('<span class=style7>')+len('<span class=style7>')
	end=html.find('</span>',beg)
	print "Rank : " +html[beg:end]