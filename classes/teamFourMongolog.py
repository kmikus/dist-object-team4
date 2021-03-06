# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-21
# Rev: 0.3

import sys, datetime
from pymongo import MongoClient

"""Module for logging events using MongoDB"""

class Logger:
    """Logging class"""

    # Server information
    SERVERNAME = "localhost"
    PORT_NUM = 27017

    def __init__(self, server=SERVERNAME, port=PORT_NUM):
        self.server = server
        self.port = port

    def prepRecord(self, eventString, payload):
        """Prepares record with timestamp before being inserted into MongoDB"""
        record = {"timestamp": datetime.datetime.utcnow(), "event": eventString, "payload": payload}
        return record

    # record should be dictionary format compatable with mongo
    def insertRecord(self, eventString, payload):
        """Peforms insert into MongoDB"""
        record = self.prepRecord(eventString, payload)
        client = MongoClient(self.server, self.port)
        db = client.dist_system_team4
        collection = db.log
        post_id = collection.insert_one(record).inserted_id
        client.close()
        return post_id

    def getCurrentIterRecords(self, time):
        """Grabs the records which have a time greater than the time input parameter"""
        result = []
        client = MongoClient(self.server, self.port)
        db = client.dist_system_team4
        collection = db.log
        for rec in collection.find({"timestamp": {"$gte": time}}).sort("timestamp"):
            result.append(rec)
        return result

    def parseTimes(self, startTime):
        """Returns the difference in times from the getCurrentIterRecords() method"""
        recTimes = []
        records = self.getCurrentIterRecords(startTime)
        for rec in records:
            if "receive" in rec["event"]:
                recTimes.append(rec["timestamp"])
        timeDiff = [recTimes[0] - startTime]
        for i in range(0, len(recTimes)-1):
            timeDiff.append(recTimes[i+1] - recTimes[i])
        return timeDiff

    def printTimes(self, startTime):
        """Prints the results of parse times in a readable format"""
        timeDiffs = self.parseTimes(startTime)
        nodes = ["Top", "Right", "Bottom", "Left"]
        messages = []
        for i in range(0, len(timeDiffs)-1):
            s = nodes[i] + " node to " + nodes[i+1] + " node time: "
            s += str(timeDiffs[i])
            messages.append(s)
        s = nodes[len(nodes)-1] + " node to " + nodes[0] + " node time: "
        s += str(timeDiffs[len(timeDiffs)-1])
        messages.append(s)
        for m in messages:
            print(m)
        return messages
        
