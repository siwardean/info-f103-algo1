import Node

class Stack:
	def __init__(self):
		self.sommet = None
		self.n = 0

	def isEmpty(self):
		return self.sommet == None

	def top(self):
		return self.sommet.data

	def size(self):
		return self.n

	def push(self, item):
		p = Node(item)
		p.setNext(self.sommet)
		self.sommet = p
		self.n += 1

	def pop(self):
		res = self.sommet.data
		self.sommet = self.sommet.next
		self.n -= 1
		return res
