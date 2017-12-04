# Project: Team 4 Distributed System Project
# Purpose Details: Send and receive a json payload via ssl
# Course: IST411
# Author: Dustin DiMarcello
# Date Developed: 2017-11-14
# Last Date Changed: 2017-12-2
# Rev: 0.3

"""Module for socket services in the distributed system"""

import socket, ssl, json

class SSLSender:
    """Sender class to reference send method"""
    def __init__(self, jsonData):
        self.json = jsonData.encode("utf-8")
        
    def createClientSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
        ssl_sock.connect(('localhost', 8081))
        return ssl_sock
        

    def send(self):
        """Sends the json through the ssl socket"""
        try:
            dustinsJson = self.json
            ssl_sock = creatClientSocket()
            ssl_sock.send(dustinsJson)
        except Exception as e:
                print(e)
                ssl_sock.close()
                
class SSLServer:
    """Base class for receiving the json payload through the socket"""
    def createServerSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s, server_side=True, certfile="server.crt", keyfile="server.key")
        ssl_sock.bind(('localhost', 8081))
        return ssl_sock
    
    def receive(self):
        """Method for receiving and returning the json data"""
        try:
            ssl_sock = createServerSocket()
            ssl_sock.listen(5)
            while True:
                (clientsocket, address) = ssl_sock.accept()
                return clientsocket.recv(2048)
        except Exception as e:
            print(e)
            ssl_sock.close()   
