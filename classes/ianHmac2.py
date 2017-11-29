# Project: Team 4 Final Project
# Purpose Details: use HMAC to modify the verify the integrity of payload message
# Course: IST 411
# Author: Ian Roach
# Date Developed: 11/26/17
# Last Date Changed: 11/26/17
# Rev: 1.0.1

import pysftp, sys, json, hmac, os

defaultSecret = "ISTRocks"

class Hmac:
	def __init__(self, secret=defaultSecret, fname):
		self.secret = secret

	def wrap(self, jsonBinData):
		body = jsonBinData.encode("utf-8")
		md5_sig = hmac.new(secret.encode(), digestmod='md5').hexdigest()
		sha1_sig = hmac.new(secret.encode(), digestmod='sha1').hexdigest()
		payload_dict['body'], payload_dict['md5'], payload_dict['sha1'] = body, md5_sig, sha1_sig
		with open(self.fname, 'w') as outFile:
			outFile.write(json.dumps(payload_dict, indent=4))

	def unwrap():
	# TODO
#		try:
#			self.connection.get('payload_team4_hmac.json')
#			with open('paylooad_team4_hmac.json', 'r') as fh:
#				decoded_json = json.load(fh)
#				message = decoded_json['message']
#				md5_rec, sha1_rec = decoded_json['md5'], decoded_json['sha1']
#				print("MD5 digest received: ", md5_rec)
#				print("SHA1 digest received: ", sha1_rec)
#				if(md5_sig == md5_rec and sha1_sig == sha1_rec):
#					print('Message verified')
#					print('Received payload')
#					print('Message: ', message)
#				else:
#					os.remove('payload_team4_hmac.json')
#					print('File removed')
#					break
#		except:
#			print('Log exception 1: ', sys.exc_info())



