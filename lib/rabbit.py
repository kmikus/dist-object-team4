#!/usr/bin/evn python

# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-10
# Rev: 0.1

# Class file for RabbitMQ Message Broker

import pika, json

testJson = {"message": "Hi"}
myJson = json.dumps(testJson)

class Broker:

	# must be a json string object
	def __init__(self, json):
		self.json = json

	# returns true to indicate successful transmission else throws exception
	def send(self):
		try:
			# setup json
			payload = json.dumps(self.json)

			# connecting
			print("Connecting to Localhost Queue")
			connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
			channel = connection.channel()

			# sending
			channel.queue_declare(queue="ist411")
			channel.basic_publish(exchange="", routing_key="ist411", body=payload)
			print(" [x] Sent json data")

			connection.close()
			return True
		except Exception as e:
			print(e)

	# returns the json as a string object
	def receive(self):
		self.respone = None
		try:
			connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
			channel = connection.channel()

			channel.queue_declare(queue="ist411")

			def callback(ch, method, properties, body):
				print(" [x] Received %r" % body)
				self.response = body
				channel.stop_consuming()

			channel.basic_consume(callback, queue="ist411", no_ack=True)

			print(" [*] Waiting for messages. To exit press CTRL+C")
			channel.start_consuming()
			return self.response
		except Exception as e:
			print(e)
