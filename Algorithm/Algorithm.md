# 参考资料
- [Github Leetcode 题解](https://github.com/qiyuangong/leetcode)
- [算法模板 Python 实现](https://github.com/dashidhy/algorithm-pattern-python)

# 使用 Python3 的一些特性
## 逻辑
进行 Coding 面试时，如果不指定使用的编程语言，一般来讲考察的是做题的思路而不是编程本身，因此不需要从零开始实现一些基础的数据结构或算法，利用语言的一些特性和自带的标准库可以大大简化代码，提高做题速度。

## 常用特性



# 二叉树
## A 遍历
```python
# 前序遍历
def PreOrder(self,root):
    # 打印二叉树（先序）
    if root == None:
        return 
    print(root.val,end=' ')
    self.PreOrder(root.left)
    self.PreOrder(root.right)

# 中序遍历
def InOrder(self,root):
    # 打印二叉树（中序）
    if root == None:
        return
    self.InOrder(root.left)
    print(root.val,end=' ')
    self.InOrder(root.right)

# 后序遍历
def BacOrder(self,root):
    # 打印二叉树（后序）
    if root == None:
        return
    self.BacOrder(root.left)
    self.BacOrder(root.right)
    print(root.val,end=' ')

# 后序非递归遍历

#层序遍历 广度优先搜索
#用队列，依次将根、左子树、右子树存入队列，按照队列的先进先出原则来实现层次遍历
def BFS(self,root):
    if roort == None:
        return
    # queue 队列 保存结点
    queue = []
    quque.append(root)

    while queue:
			# 拿出队首节点
			currentNode = queue.pop(0)
			#vals.append(currentNode.val)
			print(currentNode.val, end=' ')
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)

# 深度优先搜索

```
