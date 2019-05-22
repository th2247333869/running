# -*-utf-8-*-

class iterativeBinarySearch(object):

	def __init__(self):
		self.name = "iterativeBinarySearch"

	# 迭代版本搜索查询
	def iterativeBinarySearch(self,items,target):
		first = 0
		last = len(items)-1
		while first<=last:
			middle = (first+last)//2
			if target == items[middle]:
				return middle
			elif target > items[middle]:
				first = middle + 1
			else:
				last = middle - 1
		return False

	def recursiveBinarySearch(self,items,target):
		if len(items) == 0:
			return False
		else:
			middle = len(items)//2
			if items[middle] == target:
				return middle
			elif items[middle] > target :
				items = items[:middle]
				return self.recursiveBinarySearch(items,target)
			else:
				items = items[middle+1:]
				return self.recursiveBinarySearch(items,target)

if __name__ == "__main__":
	ite = iterativeBinarySearch()
	lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(ite.iterativeBinarySearch(lists,3))
	print(ite.recursiveBinarySearch(lists,3))

