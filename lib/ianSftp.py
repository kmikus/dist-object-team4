import pysftp, sys, json
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'oz-ist-linux-fa17-411','username':'ftpuser','password':'test1234','port': 101}

class Client:
    def __init__(self, fname):
        self.connection = pysftp.Connection(**cinfo)
        self.fname = fname
        # print('Connection successful')

    # Get fname from return value of file write method
    def put(self):
        self.connection.put(self.fname, remotepath='/home/ftpuser/payloadTeam4.json')
        return self.fname

    def get(self, getFilename):
        self.connection.get(getFilename)
        fh = open(getFilename, "r")
        payload = fh.read()
        return payload
