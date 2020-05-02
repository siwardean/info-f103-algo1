import Node

class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		base.setNext(temp)

	def length(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True 
			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = None
		current = self.head
		found = False
		while current != None and not found:
			if current is base:
				found = True
			else:
				previous = current 
				current = current.getNext()
		if found:
			if previous != None:
				previous.setNext(base.getNext())
			else:
				self.head = base.getNext()
