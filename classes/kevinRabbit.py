#!/usr/bin/evn python

# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-2
# Rev: 0.4

"""Module for rabbit, curl, and encryption services in distributed system"""

import pika, json, sys, urllib.parse, urllib.request, signal
from Crypto.Cipher import AES

# Connection settings
SERVERNAME = "localhost"
QUEUENAME = "team4"

class BrokerBase:
	"""Base class for Rabbit Sender and Receiver subclasses"""

	def connect(self):
		"""Initializes connection settings to rabbitMQ broker"""
		print("Connecting to Localhost Queue")
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(SERVERNAME))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue=QUEUENAME, durable=True)

class Sender(BrokerBase):
	"""Sends json data through rabbitmq"""

	def __init__(self, binData):
		"""Initialize with binary json data to send and start connection"""
		self.binData = binData
		self.connect()

	def send(self):
		"""Sends message to queue"""
		try:
			# setup json
			payload = self.binData

			# sending
			self.channel.basic_publish(exchange="", routing_key=QUEUENAME, body=payload)
			# print(" [x] Sent json data")

			self.connection.close()
			return payload
		except Exception as e:
			print(e)

class Receiver(BrokerBase):
	"""Listens for incoming rabbitMQ send requests"""

	def __init__(self):
		"""Starts connection"""
		self.connect()

	def receive(self):
		"""Returns the json response and stops the rabbit listener"""
		self.respone = None
		try:
			def callback(ch, method, properties, body):
				# print(" [x] Received data")
				self.response = body

				# stops listening
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

class Curler:
	"""Uses curl to fetch json from internet"""

	def __init__(self, url):
		"""Initialize with url string to get json"""
		self.url = url

	def getJson(self): 
		"""Returns json fetched from url"""
		try:
			# clean url for parsing
			clean_url = urllib.parse.urlparse(self.url)

			# request body from url
			response = urllib.request.urlopen(clean_url.geturl())
			payload = response.read()
			encoding = response.info().get_content_charset("utf-8")

			# convert to json format
			jsonStream = json.loads(payload.decode(encoding))
			jsonDump = json.dumps(jsonStream, indent=4)
			return jsonDump
		except:
			e = sys.exc_info()[0]
			print("error: {}".format(e))

class Encryptor:
	"""Encrypts the payload"""

	# Default settings
	padding = b" "
	defaultKey = "This is a key123"
	defaultIV = "This is an IV456"

	def __init__(self, data, key=defaultKey, iv=defaultIV):
		"""Accepts binary data input, uses default key and IV settings unless others are specified"""
		self.data = data
		self.key = key
		self.iv = iv

	def pad(self):
		"""Helper method to get text to mod16 bits"""
		plaintext = self.data.encode("utf-8")
		length = 16 - (len(plaintext)%16)
		plaintext += length*Encryptor.padding
		return plaintext

	def encrypt(self):
		"""Returns ciphertext of data member"""
		try:
			plaintext = self.pad()
			obj = AES.new(self.key, AES.MODE_CBC, self.iv)
			ciphertext = obj.encrypt(plaintext)
			return ciphertext
		except Exception as e:
			print(e)

class Decryptor:
	"""Decrypts the payload"""
	# TODO possibly refactor into one base class for init method?

	# Default settings
	defaultKey = "This is a key123"
	defaultIV = "This is an IV456"

	def __init__(self, data, key=defaultKey, iv=defaultIV):
		"""Accepts binary data input, uses default key and IV settings unless others are specified"""
		self.data = data
		self.key = key
		self.iv = iv

	def decrypt(self):
		"""Returns plaintext of data member"""
		obj2 = AES.new(self.key, AES.MODE_CBC, self.iv)
		decrypted = obj2.decrypt(self.data).strip()
		return decrypted.decode("utf-8") 
