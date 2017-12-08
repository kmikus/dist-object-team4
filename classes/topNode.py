# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

"""
Top node module
First: Top node starts by using cURL to retreive a JSON payload
Second: Sends the binary data over SSL on localhost:8081 
Third: Waits to receive a RabbitMQ message
Fourth: Decrypts the payload
Fifth: Finally prints ending JSON payload in utf-8 and roundtrip/point-to-point times
"""

import kevinRabbit, dustinSocket, teamFourMongolog, datetime

if __name__ == "__main__":
	try:
		# Start logging
		startTime = datetime.datetime.utcnow()
		log = teamFourMongolog.Logger()
		log.insertRecord("Top node start", None)

		# Using cURL to fetch initial JSON 
		url = "https://jsonplaceholder.typicode.com/posts/1/comments" 
		payload = kevinRabbit.Curler(url).getJson()

		# Validate that payload exists, else exit
		if not payload:
			print("There was an error fetching the payload from", url)
			exit()
		input("Please run rightNode.py and then hit enter ")

		# Send data via SSL
		mySender = dustinSocket.SSLSender(payload)
		if not mySender.send():
			print("Have you ran rightNode.py before hitting enter? Please try again")
			exit()
		log.insertRecord("Top node send", payload)

		# Listen for rabbit messages
		rabRecr = kevinRabbit.Receiver()
		rabRecr.clearQueue()
		payload = rabRecr.receive()

		# Decrypt payload
		payload = kevinRabbit.Decryptor(payload).decrypt()

		# Final results
		print(payload)
		print("\nRound trip successful!")
		log.insertRecord("Top node receive", payload)

		# Get time information
		stopTime = datetime.datetime.utcnow()
		roundtripTime = stopTime - startTime
		print("Round trip time: ", roundtripTime)

		# Uses log to print point to point times
		log.printTimes(startTime)
	except Exception as e:
		print(e)
		"An error occurred while running topNode.py"
