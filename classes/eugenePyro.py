# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/framew$# Course: IST411
# Author: Eugene Matavitski
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-1
# Rev: 0.3
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
                return payload

@Pyro4.expose
class Sender(object):
        def __init__(self):
                pass
        _data = ""
        _iteration = 0
        _uri = ''
        _daemon = Pyro4.Daemon(host=SERVERNAME)
        def startPyro(self):
                print("starting pyro")
                ns = Pyro4.locateNS()
                self._uri = self._daemon.register(self)
                ns.register("myPyro", self._uri)
                self._daemon.requestLoop()
        def set_data(self, data):
                self._data = data
        def get_compress(self):
                try:
                        print("Compressing the Payload and sending as object")
                        self._iteration +=1
                        return zlib.compress(self._data)
                except Exception as e:
                        print(e)
        def get_checksum(self):
                print("Calculating and returning checksum")
                return zlib.crc32(self._data)
        def get_iteration(self): 
                return self._iteration
        def kill_pyro(self):
                print("Killing daemon")
                Pyro4.core.Daemon.shutdown(self._daemon)
