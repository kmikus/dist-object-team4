import json, rabbit, socket, ssl, pika
from socketTeam4 import *


sender = socket.SSLSender()
sender.Send()

receiver = socket.SSLServer()
output = receiver.Receive()

print(output)
