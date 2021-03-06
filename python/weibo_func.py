#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from weibopy.api import API
from weibo import APIClient
import sys,os,urllib,urllib2,cookielib,httplib
import webbrowser
import urlparse


TEXT_WEIBO = 1
PICTURE_WEIBO = 2
TEMPRATURE_WEIBO = 3
############################################################################
def get_code(): 
	'模拟授权并且获取回调地址上的code，以获得acces token和token过期的UNIX时间'
	APP_KEY = '1315370602' #你申请的APP_KEY
	APP_SECRET = '1c1688bbd40584f65bef2f202282aaa1' #你申请的APP_SECRET 
	#回调地址，可以用这个默认地址
	CALLBACK_URL = 'http://timonkun.me' 
	AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
	USERID = 'timonkun9999@gmail.com' #微博账号
	PASSWD = 'SAw7895123' #微博密码

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

def send_weibo(weibo_type, **keystring):

	APP_KEY = '1315370602' # app key
	APP_SECRET = '1c1688bbd40584f65bef2f202282aaa1' # app secret
	CALLBACK_URL = 'http://timonkun.me' # callback url

	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

	code = get_code()

	r = client.request_access_token(code)
	print r
	access_token = r.access_token # 新浪返回的token
	expires_in = r.expires_in # token过期的UNIX时间

	client.set_access_token(access_token, expires_in)

	#

	#
	countStr = keystring['c']
	timeStr = keystring['t']
	gbkStr = countStr + timeStr + " detect human coming! @K_K鲲 -from RPi"
	#unicodeStr = gbkStr.decode('utf-8')
	unicodeStr = unicode(gbkStr, 'utf-8')

	##发普通微博
	if weibo_type == TEXT_WEIBO:
		client.statuses.update.post(status=unicodeStr)
	elif weibo_type == PICTURE_WEIBO:
		#发图片微博
		f = open('./test.jpg', 'rb')
		r = client.statuses.upload.post(status=unicodeStr, pic=f)
		f.close() ## APIClient不会自动关闭文件，需要手动关闭 
	elif weibo_type == TEMPRATURE_WEIBO:
		tempratureStr = keystring['h']
		gbkStr = countStr + timeStr + tempratureStr + " @K_K鲲 -from RPi"
		unicodeStr = unicode(gbkStr, 'utf-8')
		client.statuses.update.post(status=unicodeStr)

###########################################################################
