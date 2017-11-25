import pyro, json

fname = "payloadTeam4.json"

fh = open(fname, "r")
jsonData = fh.read()
fh.close()

Sender = pyro.Sender()
test = Sender.startPyro(jsonData)
