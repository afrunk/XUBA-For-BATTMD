# 参考资料
- [算法模板 Python 实现](https://github.com/dashidhy/algorithm-pattern-python)
- [Python Docs](https://docs.python.org/3/howto/sorting.html)
- [Leetcode Python 题解和分类](https://github.com/Jack-Cherish/LeetCode)
- [Leetcode 题解 无分类 全包含](https://github.com/liuchuo/LeetCode)

## 刷题范围
- [算法模板 Python 实现的习题](https://github.com/dashidhy/algorithm-pattern-python)
- [Leetcode 卡片](https://leetcode-cn.com/explore/)
- [LeetCode 热题100](https://leetcode-cn.com/problemset/leetcode-hot-100/)
- [牛客名企试题](https://www.nowcoder.com/ta/job-code-high)
- [剑指 Offer](https://www.nowcoder.com/ta/coding-interviews)

# 使用 Python3 的一些特性
## 逻辑
进行 Coding 面试时，如果不指定使用的编程语言，一般来讲考察的是做题的思路而不是编程本身，因此不需要从零开始实现一些基础的数据结构或算法，利用语言的一些特性和自带的标准库可以大大简化代码，提高做题速度。

## 语法补充
### A -> 的作用
-> _Attrs 常常出现在 Python 函数定义的函数名后面，为函数添加元数据，描述函数的返回类型，从而方便开发人员使用。比如
```python
def add(X , Y) -> int:
    return x + y
```

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
