100. Same Tree
---

### 1.
Use Recursion. Check every value of the root node, and recursively check its subtrees `node.left` and `node.right`. The same tree should content with both return value of `node.left` and `node.right` are `True`.

``` python
class Solution(object):
    def isSameTree(self, p, q):
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
```


### 2.
Remember the edge case:

If both trees are empty then return `True`. If one is empty another is not, return `False`.

``` python
if p is None and q is None:
    return True
if p is None or q is None:
    return False
```


### 3.
The time complexity will be according to the tree with lesser number of nodes. Let number of nodes in two trees be m and n then complexity of sameTree() is O(m) where m < n.


### 4.
Solve with iterative way.




Reference
---
- [Write Code to Determine if Two Trees are Identical][R1]
- [Iterative function to check if two trees are identical][R2]

[R1]: http://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
[R2]: http://www.geeksforgeeks.org/iterative-function-check-two-trees-identical/

