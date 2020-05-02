class Node :
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.previous = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrevious(self):
		return self.previous

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

	def setPrevious(self, newprevious):
		self.previous = newprevious
