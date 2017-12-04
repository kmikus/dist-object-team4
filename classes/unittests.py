# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-2
# Rev: 0.4

# Unit tests

<<<<<<< HEAD
import unittest, teamFourMongolog, kevinRabbit, eugenePyro, zlib, dustinSocket, datetime, ianEmail, ianHmac, ianSftp, threading
=======
import unittest, teamFourMongolog, kevinRabbit, eugenePyro, zlib, dustinSocket, datetime, threading
>>>>>>> 99ba8c06269a00523075dfbebdf27dc031ff69f9

# DO NOT EDIT THESE VALUES
testJson = '{"test": "test"}'
testBinJson = b'{"test": "test"}'
testJsonEncrypted = b'\x9b\xc5\x1dQm\x82\x99b\xf8\xc2\xe5\xac\x19\xcb\xf7\xb5f\x08\x0c\x8b\x87\xa5\xd8\xa1\xfb\x01\x1a\xa4\xf3kG\x88'
testEventString = "receive"
testPayload = b"Testing"
url = "https://jsonplaceholder.typicode.com/posts/1/comments"

class MongologTest(unittest.TestCase):
    
    def setUp(self):
        self.log = teamFourMongolog.Logger()
        self.testRecord = self.log.prepRecord(testEventString, testPayload)
        self.t = datetime.datetime.utcnow()

    def tearDown(self):
        self.log = None

    # Methods testing

    def test_prepRecord(self):
        self.assertEqual(len(self.testRecord), 3)
        self.assertIs(type(self.testRecord), dict)

    def test_insertRecord(self):
        self.assertIsNot(self.log.insertRecord(testEventString, testPayload), None)

    def test_getCurrentIterRecords(self):
        self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.getCurrentIterRecords(self.t), None)
        self.assertIs(type(self.log.getCurrentIterRecords(self.t)), list)

    def test_parseTimes(self):
        for i in range(0, 3): self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.parseTimes(self.t), None)
        self.assertIs(type(self.log.parseTimes(self.t)), list)

    def printTimes(self):
        for i in range(0, 3): self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.printTimes(self.t), None)
        self.assertIs(type(self.log.printTimes(self.t)), list)

class KevinRabbitTest(unittest.TestCase):

    # Creating objects for testing
    def setUp(self):
        self.sender = kevinRabbit.Sender(testJson)
        self.receiver = kevinRabbit.Receiver()
        self.curler = kevinRabbit.Curler(url)
        self.encryptor = kevinRabbit.Encryptor(testJson)
        self.decryptor = kevinRabbit.Decryptor(testJsonEncrypted)

    def tearDown(self):
        self.sender = None
        self.receiver = None
        self.curler = None
        self.encryptor = None
        self.decryptor = None

    # Methods testing

    def test_send(self):
        self.assertTrue(self.sender.send())

    def test_receive(self):
        self.sender.send()
        self.assertIsNot(self.receiver.receive(), None)

    def test_getJson(self):
        self.assertIsNot(self.curler.getJson(), None)

    def test_pad(self):
        self.assertEqual(len(self.encryptor.pad()), 32)
        self.assertIsNot(self.encryptor.pad(), None)

    def test_encrypt(self):
        self.assertEqual(len(self.encryptor.encrypt()), 32)
        self.assertIsNot(self.encryptor.encrypt(), None)

    def test_decrypt(self):
        ciphertext = self.encryptor.encrypt()
        self.assertEqual(self.decryptor.decrypt(), testJson)
        self.assertIs(type(self.decryptor.decrypt()), str)

class EugenePyroTest(unittest.TestCase):
        
        # Creating objects for testing
        def setUp(self):
                self.client = eugenePyro.Client()
                self.sender = eugenePyro.Sender()
        def tearDown(self):
                self.sender = None
                self.client = None

        # Methods testing

        def testDataSet(self):
                self.sender.set_data(testJson)
                self.assertIsNot(self.sender.get_data(), None)
                self.assertEqual(testJson, self.sender.get_data())

        def testCompression(self):
                self.sender.set_data(testJson.encode())
                compressed_obj = self.sender.get_compress()
                data = self.client.get_decompress(compressed_obj)
                data = data.decode("utf-8")
                self.assertEqual(testJson, data)
        def testChecksum(self):
                self.sender.set_data(testJson.encode())
                self.assertEqual(zlib.crc32(testJson.encode()), self.sender.get_checksum())

class DustinSocketTest(unittest.TestCase):
           # Creating objects for testing
       def setUp(self):
               self.sender = dustinSocket.SSLSender(testJson)
               self.server = dustinSocket.SSLServer()
       def tearDown(self):
               self.sender = None
               self.client = None

       # Methods testing

       def test_send(self):
           self.assertTrue(self.sender.createClientSocket())
       
       def test_send(self):
           self.assertTrue(self.server.createServerSocket())

class IanEmailTest(unittest.TestCase):

	# Creating objects for testing
	def setUp(self):
		self.email = ianEmail.Email('test','iar5060@psu.edu','iar5060@psu.edu')

	def tearDown(self):
		self.email = None

	# Methods testing
	def test_sendMail(self):
		self.assertTrue(self.email.sendMail(testJson))

class IanHmacTest(unittest.TestCase):

	# Creating objects for testing
	def setUp(self):
		self.hmac = ianHmac.Hmac()

	def tearDown(self):
		self.hmac = None

	# Methods testing
	def test_wrap(self):
		self.assertTrue(self.hmac.wrap(testBinJson))

	def test_unwrap(self):
		self.assertIsNot(self.hmac.unwrap(), None)

class IanSftpTest(unittest.TestCase):

	# Creating objects for testing
	def setUp(self):
		self.client = ianSftp.Client()

	def tearDown(self):
		self.client = None

	# Methods testing
	def test_put(self):
		self.assertTrue(self.client.put("payloadTeam4.json"))

	def test_get(self):
		self.assertIsNot(self.client.get("payloadTeam4.json"), b'')

=======

        
    def test_server(self):
        server = dustinSocket.SSLServer()
        server_thread = threading.Thread(target=server.receive())
        server_thread.start()
        
        time.sleep(0.000001)
        
        fake_client = socket.socket()
        fake_client.settimeout(1)
        fake_client.connect(('127.0.0.1', 7777))
        fake_client.close()
        
        server_thread.join()
    
    def run_fake_server(self):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 7777))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    def test_client(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()
    
        client = dustinSocket.SSLSender(testJson)
        client.send()
    
        server_thread.join()
>>>>>>> 99ba8c06269a00523075dfbebdf27dc031ff69f9

# keep at bottom
if __name__ == "__main__":
        unittest.main(buffer=True)

