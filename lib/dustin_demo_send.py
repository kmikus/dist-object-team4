import json, rabbit, socket, ssl, pika, socketTeam4

fakeJson = b'{"blah": "blah"}'

# receiver = socketTeam4.SSLServer()
# output = receiver.receive()

sender = socketTeam4.SSLSender(fakeJson)
sender.send()

