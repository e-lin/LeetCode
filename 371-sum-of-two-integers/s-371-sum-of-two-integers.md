371. Sum of Two Integers
---

#### 1.

`(a ^ b)` is "summing" the bits of `a` and `b`.

For example, 20(10100b) + 9(1001b):

```
10100
 1001
-----
11101
```
11101b = 29.

But this fails when you have a carry.

For example, 20(10100b) + 20(10100b):

```
10100
10100
-----
00000
```
Apparently this is wrong.


#### 2.

`(a & b) << 1` represents the `carry` for each position.

For example, 20(10100b) + 20(10100b):

```
# 1st iteration (a is 20, b is 20)
10100 ^ 10100 == 00000 # makes a 0
(10100 & 10100) << 1 == 101000 # makes b 40

# 2nd iteration:
00000 ^ 101000 == 101000 # makes a 40
(00000 & 101000) << 1 == 0000000 # makes b 0
```
Now `b` is `0`, we are done, so return `a`. This algorithm works in general, not just for the specific cases I've outlined.


#### 3.

All the masks are doing is ensuring that the value is an integer.

Since the maximum possible `int` (32 bits) is 2147483647(memorize it with hex `0xFFFFFFF`). So, if you add 2 to this value, without using mask, you will just get

```
print get_sum(2147483647, 2)
```
outputs
```
2147483649
```

with using the mask,

outputs
```
-2147483647
```
due to the overflow.


#### 4.

Python doesn't respect the `int` boundary that other strongly typed languages like Java and C++ have defined.

In C++:
``` c++
class Solution {
public:
    int getSum(int a, int b) {
        int mask = 0xFFFFFFFF;
        while (b) {
            int sum = (a ^ b) & mask;
            int carry = ((a & b) << 1) & mask;
            a = sum;
            b = carry;
        }
        return a;
    }
};
```
C++ does not need to force check the int32 boundary. While in Python:

``` python
class Solution(object):
    def getSum(self, a, b):

        MAX_INT = 0x7FFFFFFF # 32 bits integer max
        MIN_INT = 0x80000000 # 32 bits integer min
        MASK = 0xFFFFFFFF #mask to get last 32 bits

        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # if a is negative, get a's 32 bits complement positive first,
        # then get 32-bit positive's Python complement negative.
        return a if a <= MAX_INT else ~(a ^ MASK)
```


Reference
---
- [Sum of Two Integers without using “+” operator in python][R1]
- [Python solution with no "+-*/%", completely bit manipulation guaranteed][R2]
- [A 3-lines python solution][R3]


[R1]: http://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python
[R2]: https://discuss.leetcode.com/topic/51999/python-solution-with-no-completely-bit-manipulation-guaranteed
[R3]: https://discuss.leetcode.com/topic/58037/a-3-lines-python-solution