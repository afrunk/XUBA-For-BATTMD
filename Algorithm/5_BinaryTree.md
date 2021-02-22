# 二叉树
## A 遍历
### A-1 递归模板

```python
# 先序
def preorder_rec(root):
	if root is None:
		return
	visit(root)
	preorder_rec(root.left)
	preorder_rec(root.right)
	return

# 中序
def inorder_rec(root):
	if root is None:
		return
	inorder_rec(root.left)
	visit(root)
	inorder_rec(root.right)
	return

# 后序
def postorder_rec(root):
	if root is None:
		return
	postorder_rec(root.left)
	postorder_rec(root.right)
	visit(root)
	return
```

### A-2 前序非递归遍历
用栈来实现
```python
class Solution:
	def preorderTraversal(self,root:TreeNode) -> List[int]:
		preorder = []
		if root is None:
			return preorder
		
		s = [root]
		while len(s) > 0:
			node = s.pop()
			preorder.append(node.val)
			if node.right is not None:
				s.append(node.right)
			if node.left is not None:
				s.append(node.left)
		return preorder
```


### A-3 中序非递归遍历
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s, inorder = [], []
        node = root
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                inorder.append(node.val)
                node = node.right
        return inorder
```

### A-4 后序非递归遍历
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        s, postorder = [], []
        node, last_visit = root, None
        
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                peek = s[-1]
                if peek.right is not None and last_visit != peek.right:
                    node = peek.right
                else:
                    last_visit = s.pop()
                    postorder.append(last_visit.val)
        
        
        return postorder
```

### A-5 DFS 深度搜索 从下向上 分治法
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        left_result = self.preorderTraversal(root.left)
        right_result = self.preorderTraversal(root.right)
        
        return [root.val] + left_result + right_result
```

### A-6 BFS 层次遍历
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels
        
        bfs = collections.deque([root])
        
        while len(bfs) > 0:
            levels.append([])
            
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                levels[-1].append(node.val)
                
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        
        return levels
```

## B 应用
> 题解 和 扩展