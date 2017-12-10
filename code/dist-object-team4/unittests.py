# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-2
# Rev: 0.4

# Unit tests

import unittest, teamFourMongolog, kevinRabbit, eugenePyro, zlib, dustinSocket, datetime, ianEmail, ianHmac, ianSftp, threading

# DO NOT EDIT THESE VALUES
testJson = '{"test": "test"}'
testBinJson = b'{"test": "test"}'
testJsonEncrypted = b'\x9b\xc5\x1dQm\x82\x99b\xf8\xc2\xe5\xac\x19\xcb\xf7\xb5f\x08\x0c\x8b\x87\xa5\xd8\xa1\xfb\x01\x1a\xa4\xf3kG\x88'
testEventString = "receive"
testPayload = b"Testing"
url = "https://jsonplaceholder.typicode.com/posts/1/comments"

"""Unit testing for all class files"""

class MongologTest(unittest.TestCase):
    """Unit tests for the teamFourMongolog module.
    The teamFourMongolog module contains the logging and timer functionality."""

    def setUp(self):
        """Creating objects and instance variables necessary for mongo unit tests."""
        self.log = teamFourMongolog.Logger()
        self.testRecord = self.log.prepRecord(testEventString, testPayload)
        self.t = datetime.datetime.utcnow()

    def tearDown(self):
        """Cleaning up previously set up objects"""
        self.log = None
        self.testRecord = None
        self.t = None

    # Methods testing

    def test_prepRecord(self):
        """Method for appending utcnow() timestamp to record and returns the dict to be used in insertRecord() method."""
        self.assertEqual(len(self.testRecord), 3)
        self.assertIs(type(self.testRecord), dict)

    def test_insertRecord(self):
        """Inserts a record into the MongoDB log collection and return the postid of the record."""
        self.assertIsNot(self.log.insertRecord(testEventString, testPayload), None)

    def test_getCurrentIterRecords(self):
        """Retrieves the records for the current loop of the system and returns them in a list.
        This will return all records (events) after topNode.py is run and will reset on each successive run."""
        self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.getCurrentIterRecords(self.t), None)
        self.assertIs(type(self.log.getCurrentIterRecords(self.t)), list)

    def test_parseTimes(self):
        """Returns all of the node to node time differences in a list.
        This works by retreiving all of the current iteration records and subtracting the difference in receive times.
        The first differences, topNode to rightNode, uses topNodes start time instead of receive."""
        for i in range(0, 3): self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.parseTimes(self.t), None)
        self.assertIs(type(self.log.parseTimes(self.t)), list)

    def printTimes(self):
        """Prints the differences in a readable format to stdout. Returns the messages in a list."""
        for i in range(0, 3): self.log.insertRecord(testEventString, testPayload)
        self.assertIsNot(self.log.printTimes(self.t), None)
        self.assertIs(type(self.log.printTimes(self.t)), list)

class KevinRabbitTest(unittest.TestCase):
    """Unit tests for the kevinRabbit module
    This includes methods for rabbitMQ, cURL, and AES Encryption."""

    def setUp(self):
        """Creating objects and instance variables necessary for kevinRabbit unit tests."""
        self.sender = kevinRabbit.Sender(testJson)
        self.receiver = kevinRabbit.Receiver()
        self.curler = kevinRabbit.Curler(url)
        self.encryptor = kevinRabbit.Encryptor(testJson)
        self.decryptor = kevinRabbit.Decryptor(testJsonEncrypted)

    def tearDown(self):
        """Cleaning up previously set up objects."""
        self.sender = None
        self.receiver = None
        self.curler = None
        self.encryptor = None
        self.decryptor = None

    # Methods testing

    def test_send(self):
        """Sends a message using to the rabbit queue. Returns true if successful."""
        self.assertTrue(self.sender.send())

    def test_receive(self):
        """Receives one message from the broker and stops consuming. Returns the message body."""
        self.sender.send()
        self.assertIsNot(self.receiver.receive(), None)

    def test_clearQueue(self):
        self.sender.send()
        self.assertTrue(self.receiver.clearQueue())

    def test_getJson(self):
        """Uses cURL to retrieve JSON from predetermined URL. Returns the JSON in utf-8."""
        self.assertIsNot(self.curler.getJson(), None)

    def test_pad(self):
        """Pads the input to a number divisible by 16 for use with AES encryption."""
        self.assertEqual(len(self.encryptor.pad()), 32)
        self.assertIsNot(self.encryptor.pad(), None)

    def test_encrypt(self):
        """Uses AES to encrypt the data in the constructor and returns the ciphertext.
        Uses a default key and IV but they can be overridden with named params."""
        self.assertEqual(len(self.encryptor.encrypt()), 32)
        self.assertIsNot(self.encryptor.encrypt(), None)

    def test_decrypt(self):
        """Decrypts the ciphertext from the constructor and returns the plaintext.
        Uses a default key and IV but they can be overridden with named params."""
        self.assertEqual(self.decryptor.decrypt(), testJson)
        self.assertIs(type(self.decryptor.decrypt()), str)

class EugenePyroTest(unittest.TestCase):
        """Creating module for testing EugenePyroTest"""
        def setUp(self):
            """Creating object for testing"""
            self.client = eugenePyro.Client()
            self.sender = eugenePyro.Sender()
        def tearDown(self):
            """Cleaning up objects"""
            self.sender = None
            self.client = None

        # Methods testing

        def testDataSet(self):
            """verifies data is not modified by class when it is set up"""
            self.sender.set_data(testJson)
            self.assertIsNot(self.sender.get_data(), None)
            self.assertEqual(testJson, self.sender.get_data())

        def testCompression(self):
            """compresses data. decompresses it with client call and verifies that data is the same"""
            self.sender.set_data(testJson.encode())
            compressed_obj = self.sender.get_compress()
            data = self.client.get_decompress(compressed_obj)
            data = data.decode("utf-8")
            self.assertEqual(testJson, data)

        def testChecksum(self):
            """ calculates checksums on client and sender and verifies that it is the same"""
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
	"""Creaing module for testing ianEmail"""
	# Creating objects for testing
	def setUp(self):
		"""Creating object for testing"""
		self.email = ianEmail.Email('test','iar5060@psu.edu','iar5060@psu.edu')

	def tearDown(self):
		"""Cleaning up objects"""
		self.email = None

	# Methods testing
	def test_sendMail(self):
		"""Tests sendMail method from ianEmail"""
		self.assertTrue(self.email.sendMail(testJson))

class IanHmacTest(unittest.TestCase):
	"""Creating module for testing ianHmac"""
	# Creating objects for testing
	def setUp(self):
		"""Creating object for testing"""
		self.hmac = ianHmac.Hmac()

	def tearDown(self):
		"""Cleaning up objects"""
		self.hmac = None

	# Methods testing
	def test_wrap(self):
		"""Method for testing wrap() from ianHmac"""
		self.assertTrue(self.hmac.wrap(testBinJson))

	def test_unwrap(self):
		"""Method for testing upwrap() from ianHmac"""
		self.assertIsNot(self.hmac.unwrap(), None)

class IanSftpTest(unittest.TestCase):
	"""Creating module for testing ianSftp"""
	# Creating objects for testing
	def setUp(self):
		"""Creating object for testing"""
		self.client = ianSftp.Client()

	def tearDown(self):
		"""Cleaning up objects"""
		self.client = None

	# Methods testing
	def test_put(self):
		"""Method for testing put() from ianSftp"""
		self.assertTrue(self.client.put("payloadTeam4.json"))

	def test_get(self):
		"""Method for testing get() from ianSftp"""
		self.assertIsNot(self.client.get("payloadTeam4.json"), b'')

# keep at bottom
if __name__ == "__main__":
        unittest.main(buffer=True)

