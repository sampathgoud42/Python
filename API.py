import requests
import json
import os
import sys
from pprint import pprint
from lxml import etree

class API:

	def __init__(self, ip, port, username, password):
		requests.packages.urllib3.disable_warnings() 
		self.url = 'https://{ip}:{port}'.format(ip=ip, port=port)
		self.session = requests.session()
		self.username = username
		self.password = password

	def  login_with_token(self):
		target_url = 'http://10.80.1.50/phpmyadmin/index.php'
		access = self.session.get(target_url)
		tree = etree.HTML(access.content)
		accessToken = tree.xpath("//input[@name='token'][@value]")[0]
		token = accessToken.get('value')
		print token
		login_data = dict(pma_username='scg', pma_password='scg', server='1', lang='zh_TW', collation_connection='utf8_general_ci', token=token)
		r = self.session.post(target_url, data=login_data, verify=False)
		print r.status_code
		print r.json
		print r.content
		print r.headers


	def  login(self):
		target_url = self.url+'/signin.asp'
		print target_url
		login_data = dict(useraccount=self.username, pwd=self.password, submitButtonName='')
		#target_url += '?from=http://www.u-car.com.tw/index.asp&useraccount='+self.username+'&pwd='+self.password+'&submitButtonName'
		print target_url
		r = self.session.post(target_url, json=login_data, verify=False)
		#r = self.session.post(target_url, data=None, verify=False)
		print r.status_code
		print r.json
		print r.content
		print r.headers
		if r.status_code != 200:
			print 'Unable to login correctly!'
		else:
			print 'Login successfully!'

	def  get_info(self, url):
		target = self.url+url
		print target
		result = self.session.get(target, verify=False)
		print result.status_code
		print result.json()

	def move_ap(self):
		zone_id = '5bb5a9d7-cd4e-4b9a-8bc1-30260880ba7f'
		ap_mac = '24:C9:A1:18:A0:C0'
		target = self.url + '/wsg/api/scg/aps/{ap_mac}/move/{zone_id}'.format(ap_mac=ap_mac, zone_id=zone_id)
		result = self.session.put(target, verify=False)
		print result.status_code
		print result.json()