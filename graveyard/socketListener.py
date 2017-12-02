import socketTeam4

fname = "payloadTeam4.json"

while True:
    print("Listenting on socket...")
    receiver = socketTeam4.SSLServer()
    payload = receiver.receive()
    print("Payload received.")

    with open(fname, "wb") as fh:
        fh.write(payload)
