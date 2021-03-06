import rabbit, json, mongolog, timer, ianSftp, socketTeam4, pyroTeam4

# START THE FOLLOWING BEFORE RUNNING
# socketListner.py, python3 -m Pyro4.naming, pyroTeam4_listener.py

# Initial URL for JSON payload to cURL in
url = "https://jsonplaceholder.typicode.com/posts/1/comments"
fname = "payloadTeam4.json"

# The void is there to give a name to positional argument in order to make the dispatcher work but it is not used
# Each lambda expression must return something to be used as the input (if required) in the next expression
steps = [
    # Kevin's Steps
	{"name": "encrypt", "action": lambda payload: rabbit.Encryptor(payload).encrypt(), "displayMessage": "Encrypting data..."},
	{"name": "rabbitSend", "action": lambda payload: rabbit.Sender(payload).send(), "displayMessage": "Sending RabbitMQ message..."},
	{"name": "rabbitReceive", "action": lambda void: rabbit.Receiver().receive(), "displayMessage": "Receiving RabbitMQ message..."},
	{"name": "decrypt", "action": lambda payload: rabbit.Decryptor(payload).decrypt(), "displayMessage": "Decrypting data..."},

    # Dustin's Steps
    {"name": "sslSend", "action": lambda payload: socketTeam4.SSLSender(payload).send(), "displayMessage": "Sending payload through SSL..."},
    # Socket listener is in separate file, TODO multithreading?
    
    # Ian's Steps
    # TODO get fname returned from Dustin's methods instead of hardcoding
    # The sftpSend step returns the filename, not the file
    {"name": "sftpSend", "action": lambda void: ianSftp.Client(fname).put(), "displayMessage": "Putting payload on FTP Server..."},
    # payload in this case is the filename, and not the json file
    {"name": "sftpReceive", "action": lambda payload: ianSftp.Client(fname).get(payload), "displayMessage": "Getting payload from FTP Server..."},

    # Eugene's Steps
	{"name": "pyroSend", "action": lambda payload: pyroTeam4.Sender(payload).send(), "displayMessage": "Sending data from Pyro4"},
	# Pyro listener is a daemon, separate file

]

# INITIALIZATION - Timer and Logger and Counter
log = mongolog.Logger()
t = timer.Stopwatch()
payload = None
i = 0

# User specifies number of iterations up to a max of 10
while True:
	maxIter = int(input("Please specify number of iterations up to a max of 10: "))
	if maxIter >= 1 and maxIter <= 10:
		break
	else:
		print("Invalid entry, try again.")

while(i < maxIter):
	print("Starting...")
	t.start()

	# First step to cURL JSON from web, rest of cycle repeats without curl, ignore after first cycle
	if (i == 0): 
		firstStep = {"name": "curl", "action": lambda void: rabbit.Curler(url).getJson(), "displayMessage": "Getting JSON data from " + url}
		payload = firstStep["action"](payload)
		record = log.prepRecord(firstStep["name"], payload)
		log.insertRecord(record)
		print(firstStep["displayMessage"])
		print("Done.")

	# Repeat rest of cycle
	for step in steps:
		payload = step["action"](payload)
		record = log.prepRecord(step["name"], payload)
		log.insertRecord(record)
		print(step["displayMessage"])
		print("Done.")
		t.split()

	t.stop()

	# Results
	print(payload)
	print("Total time: ", t.getFormattedTotalTime())
	# TODO change timer so that the steps are associated to their times
	print("Step times: ", t.getFormattedSplitTimes())
	print("Cycle finished")
	print("\n"*3)

	i += 1
