import pyro, json
testJson = {"message": "I am the message"}
Sender = pyro.Sender()
test = Sender.startPyro(testJson)

