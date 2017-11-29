# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-29
# Rev: 0.4

import kevinRabbit, dustinSocket

# curling in JSON
url = "https://jsonplaceholder.typicode.com/posts/1/comments" 
payload = kevinRabbit.Curler(url).getJson()

# send via socket
mySender = dustinSocket.SSLSender(payload)
mySender.send()

# listen for rabbit messages
rabRecr = kevinRabbit.Receiver()
payload = rabRecr.receive()

# decrypt payload
payload = kevinRabbit.Decryptor(payload).decrypt()
print(payload)
