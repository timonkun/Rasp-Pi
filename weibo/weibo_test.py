#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from weibopy.api import API
from weibo import APIClient
import sys,os,urllib,urllib2,cookielib,httplib
import webbrowser
import urlparse

#
def get_code(): 
	APP_KEY = '1315370602' #APP_KEY
	APP_SECRET = '1c1688bbd40584f65bef2f202282aaa1' #APP_SECRET 
	#
	CALLBACK_URL = 'http://timonkun.me' 
	AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
	USERID = 'timonkun9999@gmail.com' #
	PASSWD = 'SAw7895123' #

	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	referer_url = client.get_authorize_url()
	print "referer url is : %s" % referer_url

	cookies = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookies)
	urllib2.install_opener(opener)

	postdata = {"client_id": APP_KEY,
		"redirect_uri": CALLBACK_URL,
		"userId": USERID,
		"passwd": PASSWD,
		"isLoginSina": "0",
		"action": "submit",
		"response_type": "code",
	}

	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
		"Host": "api.weibo.com",
		"Referer": referer_url
	}

	req = urllib2.Request(
	url = AUTH_URL,
	data = urllib.urlencode(postdata),
	headers = headers
	)
	try:
		resp = urllib2.urlopen(req)
		#print "callback url is : %s" % resp.geturl()
		code = resp.geturl()[-32:]
		#print "code is : %s" % resp.geturl()[-32:]
	except Exception, e:
		print e
	return code

def begin():

	APP_KEY = '1315370602' # app key
	APP_SECRET = '1c1688bbd40584f65bef2f202282aaa1' # app secret
	CALLBACK_URL = 'http://timonkun.me' # callback url

	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

	code = get_code()

	r = client.request_access_token(code)
	print r
	access_token = r.access_token # token
	expires_in = r.expires_in # 

	client.set_access_token(access_token, expires_in)

	#

	#
	gbkStr = "Hello @K_K鲲 -from RPi"
	#unicodeStr = gbkStr.decode('utf-8')
	unicodeStr = unicode(gbkStr, 'utf-8')
	client.statuses.update.post(status=unicodeStr)

	#f = open('./test.jpg', 'rb')
	#r = client.statuses.upload.post(status=unicodeStr, pic=f)
	#f.close() # 

begin() 
