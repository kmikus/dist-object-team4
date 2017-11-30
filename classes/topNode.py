# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import kevinRabbit, dustinSocket, teamFourMongolog

log = teamFourMongolog.Logger()
log.insertRecord("Starting top node", None)

# curling in JSON
url = "https://jsonplaceholder.typicode.com/posts/1/comments" 
payload = kevinRabbit.Curler(url).getJson()

input("Please run rightNode.py and then hit enter ")

# send via socket
mySender = dustinSocket.SSLSender(payload)
mySender.send()
log.insertRecord("Top node send", payload)

# listen for rabbit messages
rabRecr = kevinRabbit.Receiver()
payload = rabRecr.receive()

# decrypt payload
payload = kevinRabbit.Decryptor(payload).decrypt()
print(payload)
print("\n Transmission successful!")
log.insertRecord("Top node receive", payload)
