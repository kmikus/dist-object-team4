import rabbit, json, mongolog, timer

url = "https://jsonplaceholder.typicode.com/posts/1/comments"

# The void is there to give a name to positional argument in order to make the dispatcher work but it is not used
steps = [
	{"name": "curl", "action": lambda void: rabbit.Curler(url).getJson(), "displayMessage": "Getting JSON data from " + url},
	{"name": "encrypt", "action": lambda payload: rabbit.Encryptor(payload).encrypt(), "displayMessage": "Encrypting data..."},
	{"name": "rabbitSend", "action": lambda payload: rabbit.Sender(payload).send(), "displayMessage": "Sending RabbitMQ message..."},
	{"name": "rabbitReceive", "action": lambda void: rabbit.Receiver().receive(), "displayMessage": "Receiving RabbitMQ message..."},
	{"name": "decrypt", "action": lambda payload: rabbit.Decryptor(payload).decrypt(), "displayMessage": "Decrypting data..."}
]

payload = None
log = mongolog.Logger()
t = timer.Stopwatch()

t.start()
for step in steps:
	payload = step["action"](payload)
	record = log.prepRecord(step["name"], payload)
	log.insertRecord(record)
	print(step["displayMessage"])
	print("Done.")
	t.split()
t.stop()
print(t.getFormattedTotalTime())
print(t.getFormattedSplitTimes())
