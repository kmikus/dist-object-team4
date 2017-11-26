import json, pyro
Client = pyro.Client()
data = Client.getJson()
print(data)
