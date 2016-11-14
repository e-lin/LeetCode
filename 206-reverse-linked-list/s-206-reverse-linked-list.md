206. Reverse Linked List
---

### 1.
This is what we expect for the reverse linked list.

![Imgur](http://i.imgur.com/Um7SIpt.png)

### 2.
We need 3 pointers to remember where the nodes are.

- `current`
- `previous`
- `preceding`

The `current.next` now points to the `node(14)`, we will reverse it to point to the `node(7)`. For preventing that after we reverse the point, we cannot find `node(14)` anymore, we need a `preceding` to memorize the `node(14)`.

![Imgur](http://i.imgur.com/YWPQfTu.png)

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


Reference
---
- [Linked List: 新增資料、刪除資料、反轉][R1]

[R1]: http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html#reverse