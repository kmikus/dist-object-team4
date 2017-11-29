# Project: Team 4 Final Project
# Purpose Details: use pysftp to get and put json payload
# Course: IST 411
# Author: Ian Roach
# Date Developed: 11/23/17
# Last Date Changed: 11/23/17
# Rev: 1.0.1

import pysftp, sys, json
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'oz-ist-linux-fa17-411','username':'ftpuser','password':'test1234','port': 101}

class Client:
    def __init__(self):
        self.connection = pysftp.Connection(**cinfo)
        # print('Connection successful')

    # Get fname from return value of file write method
    def put(self, fname):
        self.connection.put(fname, remotepath='/home/ftpuser/payloadTeam4.json')
        return fname

    def get(self, fname):
        self.connection.get(fname)
        fh = open(fname, "rb")
        payload = fh.read()
        return payload