# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-2
# Rev: 0.4

# Unit tests

import unittest, kevinRabbit, eugenePyro, zlib

testJson = '{"test": "test"}'
url = "https://jsonplaceholder.typicode.com/posts/1/comments"

class KevinRabbitTest(unittest.TestCase):

	# Creating objects for testing
	def setUp(self):
		self.sender = kevinRabbit.Sender(testJson)
		self.receiver = kevinRabbit.Receiver()
		self.curler = kevinRabbit.Curler(url)
		self.encryptor = kevinRabbit.Encryptor(testJson)
		self.decryptor = kevinRabbit.Decryptor(testJson)

	def tearDown(self):
		self.sender = None
		self.receiver = None
		self.curler = None
		self.encryptor = None
		self.decryptor = None

	# Methods testing

	def test_getJson(self):
		self.assertIsNot(self.curler.getJson(), None)

	def test_pad(self):
		self.assertEqual(len(self.encryptor.pad()), 32)
		self.assertIsNot(self.encryptor.pad(), None)

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

# keep at bottom
if __name__ == "__main__":
        unittest.main()

