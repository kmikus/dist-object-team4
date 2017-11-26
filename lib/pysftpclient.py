import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
hostname = input("What is your ip address?")
cinfo = {'cnopts':cnopts, 'host':hostname, 'username':'ftpuser', 'password':'test1234', 'port':101}

try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection made")
		try:
			print("getting payload.json file")
			sftp.put('payloadTeam4.json')
			sftp.get('payloadTeam4.json')
		except:
			print("Log exception 1: ", sys.exc_info()[0])
except:
	print("Log exception 2: ", sys.exc_info()[0])
