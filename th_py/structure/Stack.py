#coding utf-8

"""
	栈（stack）在计算机科学中是
	限定仅在表尾进行插入或删除
	操作的线性表。栈是一种数据
	结构，它按照后进先出的原则
	存储数据，先进入的数据被压
	入栈底，最后的数据在栈顶，
	需要读数据的时候从栈顶开始
	弹出数据。栈是只能在某一端
	插入和删除的特殊线性表。用
	桶堆积物品，先堆进来的压在
	底下，随后一件一件往上堆。
	取走时，只能从上面一件一件
	取。读和取都在顶部进行，底
	部一般是不动的。栈就是一种
	类似桶堆积物品的数据结构，
	进行删除和插入的一端称栈顶
	，另一端称栈底。插入一般称
	为进栈，删除则称为退栈。 
	栈也称为后进先出表
"""
class Stack(object):

	#init 初始化方法
	def __init__(self , size = 8):
		self.stack = []
		self.size = size
		self.top = -1 # 栈顶位置

	# 栈内是否有数据
	def is_empty(self):
		if self.top == -1:
			return True
		else:
			return False

	# 栈是否会溢出
	def is_full(self):
		if self.top+1 == self.size:
			return True
		else:
			return False

	def push(self , data):
		if self.is_full():
			raise Exception("stack is full")
		else:
			self.stack.append(data)
			self.top+=1

	def pop(self):
		if self.is_empty():
			return Exception("stack is empty")
		else:
			self.stack.pop()
			self.top -= 1

	def display(self):
		print(str(self.stack))

# main　测试方法

stack =  Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(2)
stack.pop()
stack.display()

