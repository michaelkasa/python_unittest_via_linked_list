class Llist:

	def __init__(self):
		self.head = None
		self.l = 0

	def length(self):
		return self.l 

	def append(self,N):
		if self.head is None:
			self.head = Node(N)
			self.l = 1
		else:
			last_node = self.head
			while last_node.get_next() is not None:
				last_node = last_node.get_next()
			last_node.set_next(Node(N))
			self.l = self.l+1

	def prepend(self,N):
		old_head = self.head
		self.head = Node(N)
		self.head.set_next(old_head)
		self.l = self.l + 1

	def get_all_vals(self):
		return [self.get_val(i) for i in range(self.l)]

	def insert(self,N,i):
		if i < 0 or i > self.l:
			raise IndexError
		if i == 0:
			old_head = self.head
			self.head = Node(N)
			self.head.set_next(old_head)
		else:
			prev_node = self.head
			for ii in range(i-1):
				prev_node = prev_node.get_next()
			next_node = prev_node.get_next()
			prev_node.set_next(Node(N))
			prev_node.get_next().set_next(next_node)
			self.l = self.l + 1

	def get_val(self,i):
		if i < 0 or i > self.l-1:
			raise IndexError
		curr_node = self.head
		for ii in range(i):
			curr_node = curr_node.get_next()
		return curr_node.get_val()

	def remove(self,i):
		if i < 0 or i > self.l-1:
			raise IndexError
		if i == 0:
			val_to_return = self.head.get_val()
			self.head = self.head.get_next()
			self.l = self.l - 1
			return val_to_return
		else:
			last_node = None
			curr_node = self.head
			for ii in range(i):
				last_node = curr_node
				curr_node = curr_node.get_next()
			val_to_return = curr_node.get_val()
			last_node.set_next(curr_node.get_next())
			self.l = self.l - 1
			return val_to_return


class Node:

	def __init__(self, N):
		self.N = N
		self.next_node = None

	def get_next(self):
		return self.next_node

	def set_next(self, next_node):
		self.next_node = next_node

	def get_val(self):
		return self.N

