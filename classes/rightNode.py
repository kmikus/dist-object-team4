# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import dustinSocket, ianSftp

# receive socket data
payload = dustinSocket.SSLServer().receive()
print(payload)

# write file to system
fname = "payloadTeam4.json"
with open(fname, "wb") as fh:
	fh.write(payload)

# TODO hash payload check

# put sftp file on server
ianSftp.Client().put(fname)

