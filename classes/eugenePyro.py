# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Eugene Matavitski
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-26
# Rev: 0.2
import Pyro4, zlib, sys, base64, json
SERVERNAME = "localhost"

class Client:
        def __init__(self):
                pass
        def getJson(self):
                object_receiver = Pyro4.Proxy("PYRONAME:myPyro")
                compressed_object = object_receiver.get_compress()
                data = compressed_object["data"]
                data = base64.b64decode(data)
                payload = zlib.decompress(data)
                print("\nServer and client checksums are equal: "
            + str(zlib.crc32(payload)==object_receiver.get_checksum()))
                return payload.decode('utf8')

@Pyro4.expose
class Sender(object):
        def __init__(self):
                pass
        _data = ""
        def startPyro(self, jsonData):
                print("starting pyro")
                self._data = jsonData
                daemon = Pyro4.Daemon(host=SERVERNAME)
                ns = Pyro4.locateNS()
                uri = daemon.register(self)
                ns.register("myPyro", uri)
                daemon.requestLoop()
        def get_compress(self):
                try:
                        print("Compressing the Payload and sending as object")
                        return zlib.compress(self._data.encode('utf8'))
                except Exception as e:
                        print(e)
        def get_checksum(self):
                print("Calculating and returning checksum")
                return zlib.crc32(self._data.encode('utf8'))
