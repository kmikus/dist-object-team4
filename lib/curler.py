# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-10
# Rev: 0.1
import sys, urllib.parse, urllib.request, json

# Class file for cURL library
class Curler:

	def __init__(self, url):
		self.url = url

	def getJson(self): 
		try:
			# clean url for parsing
			clean_url = urllib.parse.urlparse(self.url)

			# request body from url
			response = urllib.request.urlopen(clean_url.geturl())
			payload = response.read()
			encoding = response.info().get_content_charset("utf-8")

			# convert to json format
			jsonStream = json.loads(payload.decode(encoding))
			jsonDump = json.dumps(jsonStream, indent=4)
			return jsonDump
		except:
			e = sys.exc_info()[0]
			print("error: {}".format(e))
