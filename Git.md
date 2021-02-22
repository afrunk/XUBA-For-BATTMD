如何使用 Git 来同步和管理 Code
<br>
参考资料：
- [Git 中文手册](https://docs.pythontab.com/github/gitbook/index.html)

# 入门
## A 关联项目的 Git 仓库
```
git remote -v   查看当前 git 关联仓库地址
git init        初始化仓库
git add *       添加所有当前信息
git commit -m 'f' 添加备注信息
git pull origin master  如果是新建仓库 就不需要下拉代码了
git push origin master  上传数据到仓库
<!-- 验证账号密码即可通过 -->


git fetch 同步远程仓库的代码
```
## A-1 更新数据
```python
git add . # 添加当前变化
git status # 查看代码的修改变化 以及各种报错的情况是什么
git commit -m '注释' #添加注释
git pull # 同步代码
# 如果在这一步报错 重新添加仓库地址
git remote rm origin
git remote add origin https://github.com/afrunk/XUBA-For-BATTMD.git


git push -u origin master # 把代码推到服务器上 master是分支的名字
git push -u origin +master# 强行更新
```

```python

```

## B 查看提交历史
```
$ git log
commit 2704e552633c41e5afd11dbe1adb244eb7ec44ce (HEAD -> master, origin/master)
Author: afrunk <afrunk7@gmail.com>
Date:   Sat Feb 20 13:42:09 2021 +0800

    f

```

## C 撤销操作
```
git commit --amend 重新提交

如果刚刚提交忘了暂存某些修改，可以先补上暂存操作，然后再运行 -amend 提交
git commit -m 'initial commit'
git add forgotten_file
git commit --amend
```
# 分支
## 创建和切换
```
git branch -a   查看所有分支
git branch      查看当前使用分支
git branch testing 创建新的分支
git checkout testing 切换分支
git branch -d branch_name 删除分支

```

## D 查看远程分支
```python
git remote show origin # 查看服务器数据库的信息
git branch -r #查看服务器的分支情况
git branch -vv # 本地分支和服务器分支的关系
git checkout origin/S1 #可以切换本地分支至服务器分支
git branch -r -d origin/S1 # 删除远程分支
#删除本地分支
git branch -d branch_name 
git push origin :branch-name 

# 如果本地没有远程分支 可以新建一个分支自动追踪远程分支
git checkout --track origin/main

# 合并分支到 master上 注意先提交分支的代码
git checkout main # 切换分支
git pull origin main  # 将远程上的代码 pull 下来
git merge master

# 查看分支合并情况
git log --graph --pretty=oneline --abbrev-commit

```