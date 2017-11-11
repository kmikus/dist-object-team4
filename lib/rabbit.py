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

# CONNECTION SETTINGS
SERVERNAME = "localhost"
QUEUENAME = "ist411"

# base class for connection settings
class BrokerBase:

	def connect(self):
		print("Connecting to Localhost Queue")
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(SERVERNAME))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue=QUEUENAME)

class Sender(BrokerBase):

	def __init__(self, json):
		self.json = json
		self.connect()

	# returns true to indicate successful transmission else throws exception
	# must be a json string object
	def send(self):
		try:
			# setup json
			payload = json.dumps(self.json)

			# sending
			self.channel.basic_publish(exchange="", routing_key=QUEUENAME, body=payload)
			print(" [x] Sent json data")

			self.connection.close()
			return True
		except Exception as e:
			print(e)

class Receiver(BrokerBase):

	def __init__(self):
		self.connect()

	# returns the json as a string object
	def receive(self):
		self.respone = None
		try:
			def callback(ch, method, properties, body):
				print(" [x] Received %r" % body)
				self.response = body
				self.channel.stop_consuming()

			self.channel.basic_consume(callback, queue=QUEUENAME, no_ack=True)

			print(" [*] Waiting for messages. To exit press CTRL+C")
			self.channel.start_consuming()
			return self.response
		# must exit program if user interruption
		except(KeyboardInterrupt, SystemExit):
			raise
		except Exception as e:
			print(e)
