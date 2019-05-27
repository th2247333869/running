# -*-utf-8-*-
class Node(object):
    def __init__(self,initData):
        self.__data = initData
        self.__next = None

    #取值
    def get(self):
        return self.__data

    #去下个值
    def getNext(self):
        return self.__next

    def setData(self,data):
        self.__data = data

    def setNext(self,next):
        self.__next = next

class SinCycLinkedlist(object):
    """初始化一个头为Node的节点对象"""
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(None)

    """新增节点"""
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self,item):
        prev = self.head
        while prev.getNext()!=self.head:
            cur = prev.getNext()
            if cur.get() == item:
                return True
            prev = prev.getNext()

    def search(self,item):
        cur = self.head.getNext() #取当前头位置的下一个节点数据
        while cur != self.head:
            if cur == item:
                return True
            cur = cur.getNext()
        return False

    def empty(self):
        if self.head.getNext() == None:
            return True
        else:
            return False

    def count(self):
        count = 0
        cur = self.head.getNext()
        if cur == None:
            return count
        while cur !=self.head:
            count = count+1
            cur = cur.getNext()
        return count








if __name__ == "__main__":
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    n5 = Node("5")

    s = SinCycLinkedlist()

    print(s.empty())
    print(s.count())





