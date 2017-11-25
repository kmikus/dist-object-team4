import ianSftp

cli = ianSftp.Client("payloadTeam4.json")
getFilename = cli.put()
payload = cli.get(getFilename)
print(payload)
