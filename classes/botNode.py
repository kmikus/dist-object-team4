# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import ianSftp, ianEmail, ianHmac, eugenePyro, teamFourMongolog

log = teamFourMongolog.Logger()
log.insertRecord("Bottom node start", None)

# pull file from sftp server
fname = "payloadTeam4.json"
payload = ianSftp.Client().get(fname)
payload = ianHmac.Hmac().unwrap().encode("utf-8")
print(payload)

log.insertRecord("Bottom node receive", payload)

emailSender = ianEmail.Email("Test subject", "kzm5599@psu.edu", "kzm5599@psu.edu")
emailSender.sendMail(payload.decode("utf-8"))

# starting pyro with payload data
pyroListener = eugenePyro.Sender()
pyroListener.loadData(payload)
print("Pyro listener running...")
print("Please run leftNode.py")
log.insertRecord("Bottom node send", payload)
pyroListener.startPyro()
