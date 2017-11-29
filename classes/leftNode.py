# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import eugenePyro, kevinRabbit

# receive pyro data
payload = eugenePyro.Client().getJson()
print(payload)

payload = payload.decode("utf-8")

# encrypt data
encPayload = kevinRabbit.Encryptor(payload).encrypt()

# send data through rabbit
kevinRabbit.Sender(encPayload).send()
