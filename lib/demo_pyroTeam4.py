import pyroTeam4

fh = open("payloadMikus.json", "rb")
data = fh.read()
fh.close()

payload = pyroTeam4.Sender(data).send()
print(payload)
