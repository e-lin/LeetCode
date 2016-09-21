283. Move Zeroes
---

- Total Accepted: 117666
- Total Submissions: 254151
- Difficulty: Easy


Problem
---
Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, `nums` should be `[1, 3, 12, 0, 0]`.

**Note:**

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.


Follow up
---
Q：如果要把所有的0放在前面而不是后面呢？A：同样的解题思路，但是是从后向前遍历，将非0数字压缩到后面。

Reference
---
[[Leetcode] Move Zeroes 移动零][R1]

[R1]: https://segmentfault.com/a/1190000003768716
