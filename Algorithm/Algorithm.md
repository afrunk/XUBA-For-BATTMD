# 参考资料
- [Github Leetcode 题解](https://github.com/qiyuangong/leetcode)
- [算法模板 Python 实现](https://github.com/dashidhy/algorithm-pattern-python)
- [Python Docs](https://docs.python.org/3/howto/sorting.html)

# 使用 Python3 的一些特性
## 逻辑
进行 Coding 面试时，如果不指定使用的编程语言，一般来讲考察的是做题的思路而不是编程本身，因此不需要从零开始实现一些基础的数据结构或算法，利用语言的一些特性和自带的标准库可以大大简化代码，提高做题速度。

## 常用特性
### A 数组初始化
```python
初始化一个长度为 N 的一维数组
N = 10
Array = [0] * N
print(Array)

# 初始化一个形状为 MxN 的二维数组（矩阵）
M = 10
matrix =[[0] * N for _ in range(M)]
print(matrix)
```

### B 交换元素值
```python
a,b = b, a
```

### C 连续不等式或等式
```python
# 判断 a, b , c 是否相等，Python 里可以直接写连等
if a == b == c:
    return true

# 不等式也可以
if a<= b<c :
    return true
```
### D 标准算法
很多语法的内容都可以通过 Python 内置的库来实现。对于 Python 而言，栈和队列都可以使用 [List As Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks) 来实现。

```python
 # 排序
 sorted() 
    # 不仅仅是对列表而言的排序 字典也可以使用
    a = [5, 2, 3, 1, 4]
    a.sort()
    a
    [1, 2, 3, 4, 5]

    # 字典
    sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
    [1, 2, 3, 4, 5]

    student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]
    sorted(student_tuples, key=lambda student: student[2])   # sort by age
    [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
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
