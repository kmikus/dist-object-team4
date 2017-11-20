import rabbit, json

url = "https://jsonplaceholder.typicode.com/posts/1/comments"

# finished step message
def fin():
	print("Done")

# cURL
print("Fetching json from ", url)
myJson = rabbit.Curler(url).getJson()
fin()

# AES Encryption
enc = rabbit.Encryptor(myJson)
print("Encrypting data...")
ciphertext = enc.encrypt()
fin()

# RabbitMQ Send
sender = rabbit.Sender(ciphertext)
sender.send()

# RabbitMQ Receive
recr = rabbit.Receiver()
receivedData = recr.receive()

# AES Decryption
dec = rabbit.Decryptor(receivedData)
print("Decrypting data...")
decryptedData = dec.decrypt()
fin()
print("Result: ", decryptedData)
