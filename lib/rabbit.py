#!/usr/bin/evn python

# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-20
# Rev: 0.3

# Class for RabbitMQ Message Broker, cURL, and AES

import pika, json, sys, urllib.parse, urllib.request, signal
from Crypto.Cipher import AES

# CONNECTION SETTINGS
SERVERNAME = "localhost"
QUEUENAME = "team4"

# base class for connection settings
class BrokerBase:

	def connect(self):
		print("Connecting to Localhost Queue")
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(SERVERNAME))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue=QUEUENAME, durable=True)

class Sender(BrokerBase):

	def __init__(self, binData):
		self.binData = binData
		self.connect()

	# returns true to indicate successful transmission else throws exception
	# must be a json string object
	def send(self):
		try:
			# setup json
			payload = self.binData

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

# Class for cURL library
class Curler:

	def __init__(self, url):
		self.url = url

	def getJson(self): 
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

# Class for AES Encryption
class Encryptor:
	padding = b" "
	defaultKey = "This is a key123"
	defaultIV = "This is an IV456"

	def __init__(self, data, key=defaultKey, iv=defaultIV):
		self.data = data
		self.key = key
		self.iv = iv

	def pad(self):
		plaintext = self.data.encode("utf-8")
		length = 16 - (len(plaintext)%16)
		plaintext += length*Encryptor.padding
		return plaintext

	def encrypt(self):
		try:
			plaintext = self.pad()
			obj = AES.new(self.key, AES.MODE_CBC, self.iv)
			ciphertext = obj.encrypt(plaintext)
			return ciphertext
		except Exception as e:
			print(e)

class Decryptor:
	# TODO possibly refactor into one base class for init method?
	defaultKey = "This is a key123"
	defaultIV = "This is an IV456"

	def __init__(self, data, key=defaultKey, iv=defaultIV):
		self.data = data
		self.key = key
		self.iv = iv

	def decrypt(self):
		obj2 = AES.new(self.key, AES.MODE_CBC, self.iv)
		decrypted = obj2.decrypt(self.data).strip()
		return decrypted.decode("utf-8") 
