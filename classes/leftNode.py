# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

"""
Left node module
First: Left node starts by calling getJson() using Pyro4 which verifies the checksum
Second: The json binary data is decoded back to utf8
Third: The payload is encrypted based on the default settings of the Encryptor class
Fourth: The payload is sent via rabbitMQ message broker using default settings
"""

import eugenePyro, kevinRabbit, Pyro4, teamFourMongolog

if __name__ == "__main__":
	# Start logging
	log = teamFourMongolog.Logger()
	log.insertRecord("Left node start", None)

	# Receive pyro data
	payload = eugenePyro.Client().getJson()
	print(payload)
	log.insertRecord("Left node receive", payload)


	# Encrypt data
	payload = payload.decode("utf-8")
	encPayload = kevinRabbit.Encryptor(payload).encrypt()

	# Send data through rabbit
	kevinRabbit.Sender(encPayload).send()
	log.insertRecord("Left node send", payload)
