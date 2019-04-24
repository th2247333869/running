# -*- coding: utf-8 -*-
# 深度优先和广度优先

class Graph(object):

	# 初始化复制
	def __init__(self,*args,**kwargs):
		self.node_neigbors = {} 
		self.visited = {}

	# 新增节点(list)
	def add_nodes(self,node_list):
		for node in node_list:
			self.add_node(node)

	def add_node(self,node):
		if not node in self.nodes():#校验当前传入node是否已经存在
			self.node_neigbors[node] = [] 

	# 返回对应节点
	def nodes(self):
		return self.node_neigbors.keys()

	# 传入顶点
	def add_edge(self,edge):
		u,v = edge #以1，2为例
		"""
			当第一次传入参数时 字典value均为[] 判断为True
		"""
		if (not v in self.node_neigbors[u]) and (not u in self.node_neigbors[v]):
			self.node_neigbors[u].append(v)
			if(u!=v):
				self.node_neigbors[v].append(u)

	# 深度优先算法
	"""
		算法讲解 假设 有如下的二叉树	
			 1
		  2    3
		4   5 6  7	

		选取定点1 寻找与其连接的定点 2、3 我们选择2 找到与其连接的点并未走过的 为4、5 我们选4 4的定点下
		没有更多定点 则回溯 2 去往下一个定点5 回溯 2 1 以此类推 3 6 3 7 结束
	"""

	def depth_first_search(self,root=None):
		order = []
		def dfs(node):
			self.visited[node] = True
			order.append(node)
			for n in self.node_neigbors[node]:
				if not n in self.visited:
					dfs(n)
		if root:
			dfs(root)
		for node in self.nodes():
			if not node in self.visited:
				dfs(node)

		print (order)
		return order

# main 测试方法

g = Graph()
g.add_nodes([i+1 for i in range(8)])
g.add_edge((1, 2))
g.add_edge((1, 3))
g.add_edge((2, 4))
g.add_edge((2, 5))
g.add_edge((4, 8))
g.add_edge((5, 8))
g.add_edge((3, 6))
g.add_edge((3, 7))
g.add_edge((6, 7))
print ("nodes:", g.nodes())
order = g.depth_first_search(1)