import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'192.168.1.45','username':'ftpuser','password':'test1234','port': 101}

class Client:
    def __init__(self):
        self.connection = pysftp.Connection(**cinfo)
        print("Connection successful")

    def get(self):
        self.connection.get('payloadTeam4.json')
        print('Received payload')

    def put(self):
        self.connection.put('payloadTeam4.json', remotepath='/home/ftpuser/payloadTeam4.json')
        print('Send payload')
