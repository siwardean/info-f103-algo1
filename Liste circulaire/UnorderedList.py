.import Node

class UnorderedList:
	def __init__(self):
		self.head = Node(-1)
		self.head.setNext(self.head)

	def isEmpty(self):
		return self.head.getNext() == self.head

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head.getNext())
		self.head.setNext(temp)

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		base.setNext(temp)

	def length(self):
		current = self.head
		count = 0
		while current != self.head:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head.getNext()
		found = False
		while current != self.head and not found:
			if current.getData() == item:
				found = True 
			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = self.head
		current = self.head.getNext()
		found = False
		while current != self.head and not found:
			if current is base:
				found = True
			else:
				previous = current 
				current = current.getNext()
		if found:
			previous.setNext(base.getNext())
