206. Reverse Linked List
---

### 1.
This is what we expect for the reverse linked list.

![Imgur](http://i.imgur.com/UxfhW8H.png)

### 2.
We need 3 pointers to remember where the nodes are.

- `current`
- `previous`
- `preceding`

The `current.next` now points to the `node(14)`, we will reverse it to point to the `node(7)`. For preventing that after we reverse the point, we cannot find `node(14)` anymore, we need a `preceding` to memorize the `node(14)`.

![Imgur](http://i.imgur.com/uNwDuCg.png)

### 3.
The whole process will be:

1. change `current.next` to point to `previous`.
2. move the 3 pointers forward.

```
previous = current
current = preceding
preceding = preceding.next
```

![Imgur](http://i.imgur.com/pau4F1R.png)

### 4.
At the final stage, the `current` will be the last node. But we need to reverse for the last time. Change `current.next` to point to `previous`. We do not need to move the 3 pointers forward anymore.

### 5.
Refresh the **head** to `current`.


Use only 2 Pointers
---
If we only have `previous` and `current` pointers.

``` python
def reverseList(self, head):
    previous = None
    while head:
        current = head
        head = head.next
        current.next = previous #inverse
        previous = current
    return previous
```


Solve with Recursion
---

``` python
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev = None):
    if node is None:
        return prev
    curr = node.next
    node.next = prev
    return self._reverse(curr, node)
```


Time Complexity
---
All solutions are `O(n)`, as we visit every node in the Linked List just once.


Reference
---
- [Linked List: 新增資料、刪除資料、反轉][R1]
- [Python Iterative and Recursive Solution][R2]

[R1]: http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html#reverse
[R2]: https://discuss.leetcode.com/topic/14043/python-iterative-and-recursive-solution