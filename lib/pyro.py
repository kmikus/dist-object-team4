import Pyro4, zlib, sys, base64
SERVERNAME = "localhost"



class Client:
        def __init__(self):
                self.json = json
                self.runSelf()

        def runSelf(self):
                object_receiver = Pyro4.Proxy("PYRONAME:myPyro")
                compressed_object = object_receiver.get_compress()

                data = compressed_object["data"]
                data = base64.b64decode(data)
                payload = zlib.decompress(data)
                print("\nServer and client checksums are equal: ")

@Pyro4.expose
class Sender(object):
        _data = ""
        def __init__(self, json):
                self._data = json
                daemon = Pyro4.Daemon(host=SERVERNAME)
                ns = Pyro4.locateNS()
                uri = daemon.register(self)
#               ns.register("myPyro", uri)
                print("eeady. object uri = ", uri)
                daemon.requestLoop()
        def get_compress(self):
                try:
                        print("Compressing the Payload and sending as object")
                        return zlib.compress(self._data)
                except Exception as e:
                        print(e)
        def get_checksum(self):
                        print("Calculating and returning checksum")
                        return zlib.crc32(self._data)

#Pyro4.Daemon.serveSimple(
#       {
#               Sender: "myPyro"
#       },
#       ns = True,
#       verbose = True,
#       host = SERVERNAME)

