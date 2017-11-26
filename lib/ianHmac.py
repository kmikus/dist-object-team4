# Project: Team 4 Final Project
# Purpose Details: use HMAC to modify the verify the integrity of payload message
# Course: IST 411
# Author: Ian Roach
# Date Developed: 11/26/17
# Last Date Changed: 11/26/17
# Rev: 1.0.1

import pysftp, sys, json, hmac, os

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'oz-ist-linux-fa17-411','username':'ftpuser','password':'test1234','port': 101}

Class HMAC:
	def __init__(self, fname):
		self.connection = pysftp.Connection(**cinfo)
		self.fname = fname


