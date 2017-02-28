226. Invert Binary Tree
---

### 1.
Recursively.

``` python
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
```

### 2.
BFS:

``` python
def invertTree(self, root):

```

### 3.




Reference
---
- [Python solutions (recursively, dfs, bfs).][R1]
- [Python one-line][R2]

[R1]: https://discuss.leetcode.com/topic/21271/python-solutions-recursively-dfs-bfs
[R2]: https://discuss.leetcode.com/topic/46630/python-one-liner