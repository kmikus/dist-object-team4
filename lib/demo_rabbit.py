import rabbit, json

testJson = {"message": "I am the message"}
myJson = json.dumps(testJson)

sender = rabbit.Sender(myJson)
sender.send()

recr = rabbit.Receiver()
print(recr.receive())
