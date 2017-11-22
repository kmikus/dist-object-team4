import time

class Stopwatch:

	def __init__(self):
		self.timelog = []
		self.running = False
		self.finished = False

	def start(self):
		if not self.running:
			self.timelog = []
			self.startTime = time.time()
			self.timelog.append(self.startTime)
			self.running = True
			self.finished = False
		else:
			print("Timer must be stopped before starting")

	def split(self):
		if self.running:
			self.timelog.append(time.time())
		else:
			print("Timer must be running first")

	def stop(self):
		if self.running:
			self.timelog.append(time.time())
			self.running = False
			self.finished = True
		else:
			print("Timer must be running first")

	def getLog(self):
		return self.timelog

	def getTotalTime(self):
		if self.finished:
			return self.timelog[-1] - self.timelog[0]
		else:
			print("Please stop the timer first")

	def getSplitTimes(self):
		if self.finished:
			splits = []
			for i in range(1, len(self.timelog)):
				splits.append(self.timelog[i] - self.timelog[i-1])
			return splits
		else:
			print("Please stop the timer first")

	def formatTime(self, secs):
		mins = secs // 60
		minsString = "{0:g}".format(mins)
		modSecs = secs % 60
		secsString = "{0:.2f}".format(modSecs)
		if modSecs < 10:
			secsString = "0" + secsString
		outputStr = minsString + ":" + secsString
		return outputStr

	def getFormattedTotalTime(self):
		return self.formatTime(self.getTotalTime())

	def getFormattedSplitTimes(self):
		formattedSplits = []
		for split in self.getSplitTimes():
			formattedSplits.append(self.formatTime(split))
		return formattedSplits
