# Project: Team 4 Final Project
# Purpose Details: use HMAC to modify the verify the integrity of payload message
# Course: IST 411
# Author: Ian Roach
# Date Developed: 11/26/17
# Last Date Changed: 11/26/17
# Rev: 1.0.1

import pysftp, sys, json, hmac, os

fname = "payloadTeam4.json"
secret = "ISTRocks"

class Hmac:

	def wrap(self, jsonBinData):
		body = jsonBinData.decode("utf-8")
		md5_sig = hmac.new(secret.encode(), digestmod='md5').hexdigest()
		sha1_sig = hmac.new(secret.encode(), digestmod='sha1').hexdigest()
		payload_dict = {}
		payload_dict['body'], payload_dict['md5'], payload_dict['sha1'] = body, md5_sig, sha1_sig
		with open(fname, 'w') as outFile:
			outFile.write(json.dumps(payload_dict, indent=4))

	def unwrap(self):
		try:
			with open (fname, "r") as fh:
				decoded_json = json.load(fh)
				body = decoded_json['body']
				md5_rec, sha1_rec = decoded_json['md5'], decoded_json['sha1']
				md5_sig = hmac.new(secret.encode(), digestmod='md5').hexdigest()
				sha1_sig = hmac.new(secret.encode(), digestmod='sha1').hexdigest()
				if(md5_sig == md5_rec and sha1_sig == sha1_rec):
					print('Digest message verified')
				else:
					os.remove(fname)
					print('File removed')
			return body
		except:
			print('Log exception 1: ', sys.exc_info())



