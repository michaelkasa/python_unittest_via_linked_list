import unittest
from Llist import Llist

class TestLinkedList(unittest.TestCase):

	def test_length(self):
		l = Llist()
		self.assertEqual(l.length(), 0)

	def test_append(self):
		l = Llist()
		l.append(1)
		l.append(2)
		l.append(3)
		self.assertEqual(l.get_all_vals(),[1,2,3])
		self.assertEqual(l.length(),3)

	def test_prepend(self):
		l = Llist()
		l.prepend(1)
		l.prepend(2)
		l.prepend(3)
		self.assertEqual(l.get_all_vals(),[3,2,1])
		
	def test_insert(self):
		l = Llist()
		for N in range(50):
			l.append(N)
		l.insert(777,25)
		self.assertEqual(l.length(),51)
		for N in range(25):
			self.assertEqual(l.get_val(N),N)
		self.assertEqual(l.get_val(25),777)
		for N in range(26,50):
			self.assertEqual(l.get_val(N+1),N)

	def test_remove(self):
		l = Llist()
		for N in range(50):
			l.append(N)
		for N in range(50):
			self.assertEqual(l.remove(0),N)
			self.assertEqual(l.get_all_vals(), 
					[n for n in range(N+1,50)])
		for N in range(10,20):
			l.append(N)
			self.assertEqual(l.length(),N-9)
		self.assertEqual(l.remove(4),14)
		self.assertEqual(l.get_all_vals(),
				[10,11,12,13,15,16,17,18,19])

	def test_index_errors(self):
		with self.assertRaises(IndexError):
			l = Llist()
			l.remove(0)
		with self.assertRaises(IndexError):
			l = Llist()
			l.get_val(0)
		with self.assertRaises(IndexError):
			l = Llist()
			l.append(25)
			l.append(30)
			l.append(35)
			l.get_val(5)
		with self.assertRaises(IndexError):
			l = Llist()
			l.append(25)
			l.append(30)
			l.append(35)
			l.insert(40,4) 

if __name__ == '__main__':
	unittest.main()
