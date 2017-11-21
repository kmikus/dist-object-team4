# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-21
# Rev: 0.3

import sys, datetime
from pymongo import MongoClient

class Logger:

	# Server information
	SERVERNAME = "localhost"
	PORT_NUM = 27017

	def __init__(self, server=SERVERNAME, port=PORT_NUM):
		self.server = server
		self.port = port

	def prepRecord(self, eventString, payload):
		record = {"timestamp": datetime.datetime.utcnow(), "event": eventString, "payload": payload}
		return record

	# record should be dictionary format compatable with mongo
	def insertRecord(self, record):
		client = MongoClient(self.server, self.port)
		db = client.dist_system_team4
		collection = db.log
		post_id = collection.insert_one(record).inserted_id
		client.close()
		return post_id

