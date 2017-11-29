# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import ianSftp, eugenePyro

# pull file from sftp server
fname = "payloadTeam4.json"
payload = ianSftp.Client().get(fname)
print(payload)

# TODO verify hmac and send via e-mail

# starting pyro with payload data
eugenePyro.Sender().startPyro(payload)
