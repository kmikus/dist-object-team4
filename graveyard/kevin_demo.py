import rabbit, json, mongolog

url = "https://jsonplaceholder.typicode.com/posts/1/comments"

# finished step message
def fin(eventString, payload):
	print(eventString)
	print("Done")
	record = log.prepRecord(eventString, payload)
	log.insertRecord(record)

# Start logger
log = mongolog.Logger()

# cURL
eventString = "Fetching json from " + url + "..."
myJson = rabbit.Curler(url).getJson()
fin(eventString, myJson)

# AES Encryption
eventString = "Encrypting data..."
enc = rabbit.Encryptor(myJson)
ciphertext = enc.encrypt()
fin(eventString, ciphertext)

# RabbitMQ Send
eventString = "Rabbit send..."
sender = rabbit.Sender(ciphertext)
payload = sender.send()
fin(eventString, payload)

# RabbitMQ Receive
eventString = "Rabbit receive..."
recr = rabbit.Receiver()
receivedData = recr.receive()
fin(eventString, receivedData)

# AES Decryption
eventString = "Decrypting data..."
dec = rabbit.Decryptor(receivedData)
decryptedData = dec.decrypt()
fin(eventString, decryptedData)

print(decryptedData)
