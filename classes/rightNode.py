# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import dustinSocket, ianSftp, ianHmac, teamFourMongolog

# This value should be false for running on IST Server, and true to run locally
fixDnsResolve = True

log = teamFourMongolog.Logger()
log.insertRecord("Right node start", None)

# receive socket data
print("Listening for socket data")
payload = dustinSocket.SSLServer().receive()
print("Data received")
print(payload)
log.insertRecord("Right node receive", payload)

# write file to system
fname = "payloadTeam4.json"
with open(fname, "wb") as fh:
	fh.write(payload)

fh = open(fname, "rb")
payload = fh.read()
fh.close()

ianHmac.Hmac().wrap(payload)

# put sftp file on server
ianSftp.Client(fixDnsResolve).put(fname)
log.insertRecord("Right node send", payload)
print("Please run botNode.py")
