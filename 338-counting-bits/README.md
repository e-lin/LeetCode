338. Counting Bits
---

- Total Accepted: 48356
- Total Submissions: 82373
- Difficulty: Medium


Problem
---
Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example:**

For `num = 5` you should return `[0,1,1,2,1,2]`.


**Follow up:**

- It is very easy to come up with a solution with run time **O(n\*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass? _**(See [Solution][R2])**_
- Space complexity should be **O(n)**.
- Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.


**Hint:**

1. You should make use of what you have produced already.
2. Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
3. Or does the odd/even status of the number help you in calculating the number of 1s?


[What is __builtin_popcount in c++?][R1]
---
There is **NO** __builtin_popcount in c++, it's a **built in function of GCC**.

The function prototype is as follows:

``` c++
 int  __builtin_popcount(unsigned int)
```

It returns the numbers of  bits in an integer (the number of ones in the binary representation of the integer).

**For example,**

``` c++
 cout<< __builtin_popcount (4);
```

The above code gives "1" as output.

_**Why to use it?**_

This function tries to use CPU specific instructions, which will always be orders of magnitude faster than any algorithm you manage to come up  with.


Related Challenges
---
`191. Number of 1 Bits`.


[R1]: https://www.quora.com/What-is-__builtin_popcount-in-c++
[R2]: https://www.hrwhisper.me/leetcode-counting-bits/