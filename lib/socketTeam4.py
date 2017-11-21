import socket, ssl, json, rabbit



class SSLSender:
    def Send(self):
        try:
            recr = rabbit.Receiver()
            dustinsJson = recr.receive()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
            ssl_sock.connect(('localhost', 8080))
            ssl_sock.send(dustinsJson)
        except Exception as e:
                print(e)
                ssl_sock.close()
                
class SSLServer:
    def Receive(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = ssl.wrap_socket(s, server_side=True, certfile="server.crt", keyfile="server.key")
            ssl_sock.bind(('localhost', 8080))
            ssl_sock.listen(5)
            while True:
                (clientsocket, address) = ssl_sock.accept()
                return clientsocket.recv(1024)
        except Exception as e:
            print(e)
            ssl_sock.close()   