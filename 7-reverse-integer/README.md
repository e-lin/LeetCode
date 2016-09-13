7. Reverse Integer
---

- Total Accepted: 165087
- Total Submissions: 693937
- Difficulty: Easy


Problem
---
Reverse digits of an integer.

Example1: x = 123, return 321

Example2: x = -123, return -321

**Have you thought about this?**

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

**Update (2014-11-10):**

Test cases had been added to test the overflow behavior.


Issue
---
### Can integers overflow in python?

Short answers:

>`No`, if the operations are done in pure python, because python integers have arbitrary precision

>`Yes`, if the operations are done in the pydata stack (numpy/pandas), because they use C-style fixed-precision integers

Therefore, to content with the test case of overflow, we need to use numpy.

To crate an overflow case:

``` python
from scipy import log1p, exp
from numpy import array, isnan

a = array([0.2222, 500.3, 0.3, 700.8, 0.111])

values = log1p(-exp(-exp(10**a - 9**a)))

print values # Note the nan's

indOverflow = isnan(values)
values[indOverflow] = 0
```
You will get a warning due to numeric overflow. To close the warning:

``` python
numpy.seterr(over='ignore')
```

### Overflow with a 32-bit integer

However, one test case is `1534236469` that we are expected to get `0` because of overflow (with a 32-bit integer). We have to make a if statement to check:

``` python
if integer < -(1 << 31) or integer > (1 << 31) - 1:
    //overflow with 32-bit integer
```


Reference
---
- [Can Integer Operations Overflow in Python?][R1]
- [How do I check for numeric overflow without getting a warning in Python?][R2]

[R1]: http://mortada.net/can-integer-operations-overflow-in-python.html
[R2]: http://stackoverflow.com/questions/9349434/how-do-i-check-for-numeric-overflow-without-getting-a-warning-in-python
