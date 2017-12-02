# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import eugenePyro, kevinRabbit, Pyro4, teamFourMongolog

log = teamFourMongolog.Logger()
log.insertRecord("Left node start", None)

# receive pyro data
payload = eugenePyro.Client().getJson()
print(payload)
log.insertRecord("Left node receive", payload)


# encrypt data
payload = payload.decode("utf-8")
encPayload = kevinRabbit.Encryptor(payload).encrypt()

# send data through rabbit
kevinRabbit.Sender(encPayload).send()
log.insertRecord("Left node send", payload)
