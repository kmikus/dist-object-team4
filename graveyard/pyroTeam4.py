import zlib, sys, Pyro4, base64

class Sender:

	def __init__(self, data):
		self.data = data

	def send(self):
		try:
			payloadComp = zlib.compress(self.data)
			checksum = zlib.crc32(self.data)

			decompressor = Pyro4.Proxy("PYRONAME:comp.decompressor")

			payloadDecomp = decompressor.decomp(payloadComp)
			payloadDecomp = base64.b64decode(payloadDecomp['data'])

			checksumGen = zlib.crc32(payloadDecomp)

			if checksum == checksumGen:
				print("Checksum matches")
			else:
				print("Error: checksum mismatch")

			return payloadDecomp.decode("utf-8")
		except Exception as e:
			print(e)

@Pyro4.expose
class Decompressor(object):
	def decomp(self, compdata):
		data = compdata["data"]
		data = base64.b64decode(data)
		payloadDecomp = zlib.decompress(data)
		return payloadDecomp

class Listener:
	
	def start(self):
		daemon = Pyro4.Daemon()

		ns = Pyro4.locateNS()
		uri = daemon.register(Decompressor)
		ns.register("comp.decompressor", uri)

		print("Ready")
		daemon.requestLoop()
