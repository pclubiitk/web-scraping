import urllib
import urllib2
import cookielib
import os
from bs4 import BeautifulSoup as bs
cj=cookielib.CookieJar()
mobileNo=raw_input('Enter mobile number : ').strip()
message=raw_input('Enter the text message : ').strip()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
values = {      'username' : '<Enter your way2sms username>',
                'password' : '<Enter your way2sms password>',
                 'gval' :''
                }
data = urllib.urlencode(values)
opener.open('http://site3.way2sms.com/Login1.action',data)
SessionID=cj._cookies['site3.way2sms.com']['/']['JSESSIONID'].value
SessionID=SessionID[4:]
print SessionID
# http://site3.way2sms.com/MainView.action?id=7D3110B0FEC7203152B2BF1756C864D0.w801

opener.addheaders = [
                 ('Host', 'site3.way2sms.com'),
                ('Host','site3.way2sms.com'),
                ('Origin','http://site3.way2sms.com'),
                ('Referer','http://site3.way2sms.com/content/index.html'),
                ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'),
                ('Accept'        , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                ('Accept-Language' , 'en-us,en;q=0.5'),
                ('Connection'    ,  'keep-alive')
                ]

opener.open('http://site3.way2sms.com/MainView.action',urllib.urlencode({'id':SessionID}))

output=opener.open('http://site3.way2sms.com/singles.action',urllib.urlencode({'Token':SessionID}))
html=output.read()
smsParams={}
beg=html.find("t_15_k_5")-100
while(1):
	paramBeg=html.find('<input',beg)
	if(paramBeg==-1):
		break
	paramEnd=html.find('>',paramBeg)
	param=bs(html[paramBeg:paramEnd+1])
	if(param.input.has_key('name')):
		if(param.input.has_key('value')):
			smsParams[param.input['name']]=param.input['value']
			if(html[paramBeg:paramEnd+1].find('Mobile Number')>=0):
				smsParams[param.input['name']]=mobileNo

		else:
			smsParams[param.input['name']]=''
	beg=paramEnd+1
beg=html.find("t_15_k_5")
while(1):
	paramBeg=html.find('<textarea',beg)
	if(paramBeg==-1):
		break
	paramEnd=html.find('</textarea>',paramBeg)
	param=bs(html[paramBeg:paramEnd+11])

	if(param.textarea.has_key('name')):
		if(len(param.textarea.contents)==0):
			smsParams[param.textarea['name']]=""
		else:
			smsParams[param.textarea['name']]=str(param.textarea.contents[0])

	beg=paramEnd+1

beg=html.find('document.createElement("input")')
HiddenName=html[html.find('name", "',beg)+8:html.find(')',html.find('name", "',beg))-1]
smsParams[HiddenName]=''

beg=html.find('document.createElement("input")',beg+10)
HiddenName=html[html.find('name", "',beg)+8:html.find(')',html.find('name", "',beg))-1]
HiddenVal=html[html.find('value", "',beg)+9:html.find(')',html.find('value", "',beg))-1]
smsParams[HiddenName]=HiddenVal
smsParams['textArea']="seskdsgfsdkt"
print smsParams
output=opener.open('http://site3.way2sms.com/stp2p.action',urllib.urlencode(smsParams))
