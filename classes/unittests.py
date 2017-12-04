# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-2
# Rev: 0.4

# Unit tests

import unittest, teamFourMongolog, kevinRabbit, eugenePyro, zlib, dustinSocket, datetime

# DO NOT EDIT THESE VALUES
testJson = '{"test": "test"}'
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
        self.sslsender = dustinSocket.SSLSender(testJson)
        self.sslserver = dustinSocket.SSLServer()

    def tearDown(self):
        self.sslsender = None
        self.sslserver = None

       # Methods testing

#    def test_send(self):
#        self.assertIsNot(self.sslsender.send(), None)
#    def test_receive(self):
#        self.assertEqual(len(self.sslserver.receive()), None)
#        self.assertIsNot(self.sslserver.receive())

# keep at bottom
if __name__ == "__main__":
        unittest.main(buffer=True)

