import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'192.168.1.45','username':'ftpuser','password':'test1234','port': 101}

class Client:
    def __init__(self, json):
        self.connection = pysftp.Connection(**cinfo)
        self.json = json
        print('Connection successful')

    def get(self):
        payload = self.json
        self.connection.get(payload)
        print('Received payload')
        return payload

    def put(self):
        payload = self.json
        self.connection.put(payload, remotepath='/home/ftpuser/payload.json')
        print('Sent payload')
        return payload
