# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/framew$# Course: IST411
# Author: Eugene Matavitski
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-1
# Rev: 0.3

"""Module for Pyro4 and compressing services"""

import Pyro4, zlib, sys, base64, json
SERVERNAME = "localhost"

class Client:
        """Class for Pyro4 client that can use registered daemon"""

        def __init__(self):
                pass
        def get_decompress(self, data):
                """decompresses object"""
                return zlib.decompress(data)
        def getJson(self):
                """Looks registered daemon, receives compressed object, docompresses and validates"""
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
        """Class for Pyro4 sender and file compressor with exposed methods"""
        def __init__(self):
                pass
        _data = ""
        _iteration = 0
        _uri = ''
        _daemon = Pyro4.Daemon(host=SERVERNAME)
        def startPyro(self):
                """Initializes Pyro daemon and starts listener"""
                print("starting pyro")
                ns = Pyro4.locateNS()
                self._uri = self._daemon.register(self)
                ns.register("myPyro", self._uri)
                self._daemon.requestLoop()
        def set_data(self, data):
                """Sets data that is compressed"""
                self._data = data
        def get_compress(self):
                """Compresses data and returns it"""
                try:
                        print("Compressing the Payload and sending as object")
                        self._iteration +=1
                        return zlib.compress(self._data)
                except Exception as e:
                        print(e)
        def get_checksum(self):
                """Calculates checksum for the original data"""
                print("Calculating and returning checksum")
                return zlib.crc32(self._data)
        def get_iteration(self):
                """Calculates number of calls for compressed data"""
                return self._iteration
        def get_data(self):
                return self._data
        def kill_pyro(self):
                """Stops Pyro listener"""
                print("Killing daemon")
                Pyro4.core.Daemon.shutdown(self._daemon)
