# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

"""Module that is responsible for actions of the right node
First: Receives docket data.
Second: Writes the file to the system.
Third: Puts the sftp file on the server.
"""

import dustinSocket, ianSftp, ianHmac, teamFourMongolog

log = teamFourMongolog.Logger()
log.insertRecord("Right node start", None)

# receive socket data
try:
	print("Listening for socket data")
	payload = dustinSocket.SSLServer().receive()
	print("Data received")
except Exception as e:
	print(e)
	print("Couldn't receive socket data..")
print(payload)
log.insertRecord("Right node receive", payload)

# write file to system
try:
	fname = "payloadTeam4.json"
	with open(fname, "wb") as fh:
		fh.write(payload)

	fh = open(fname, "rb")
	payload = fh.read()
	fh.close()
except Exception as e:
	print(e)
	print("Something went wrong")
ianHmac.Hmac().wrap(payload)

# put sftp file on server
try:
	ianSftp.Client().put(fname)
	log.insertRecord("Right node send", payload)
except Exception as e:
	print(e)
	print("Couldn't put sftp file on server")
print("Please run botNode.py")
