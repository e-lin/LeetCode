438. Find All Anagrams in a String
---

### 1.
An example to the goal:

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
is to find out all the start indices of `p`'s anagrams in `s`.


### 2.
The first thought to the challenge was very brute. It has 2 loops for `s` and `p`.

``` python
l = []
for i in xrange(len(s)-len(p)+1):
    temp = list(p[:])
    for j in xrange(len(p)):
        if s[i+j] in temp: temp.remove(s[i+j])

    if len(temp) == 0: l.append(i)

return l
```
In this case we have `O(n^2)`, and `s[i+j] in temp` would be `O(n)`. As `s` and `p` will not be larger than 20,100, if we have `s` and `p` with string length of `10^5` respectively, the computer cannot afford it. (It's better within `10^6`) Apparently, it ended up with Time Limit Exceeded.


### 3.
The second try to the challenge is to visit `s` only instead of visiting `s` and `p`.

``` python
d = {}
for i in xrange(len(s)-len(p)+1):
    slst = list(s[i:i+len(p)])
    slst.sort()
    ssorted = "".join(slst)

    if ssorted not in d:
        d[ssorted] = [i]
    else:
        d[ssorted] += [i]

plst = list(p)
plst.sort()
psorted = "".join(plst)
return d[psorted] if psorted in d else []
```
With the case of

```
s = "cbaebabacd"
p = "abc"
```
We get

```
d = {'abb': [4], 'abc': [0, 6], 'abe': [1, 2, 3], 'acd': [7], 'aab': [5]}
```

However, We will still get **TLE** when running all the test cases. Since I sorted the substring in each run. Which is `O(nlogn)` time, the total time complexity for this solution would be `O(n*nlogn)`.


### 4.
A O(n^2) solution would be like this:

``` python
def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    cp = collections.Counter(p)
    cs = collections.Counter()
    ans = []
    for i in range(len(s)):
        cs[s[i]] += 1
        if i >= len(p):
            cs[s[i - len(p)]] -= 1
            if cs[s[i - len(p)]] == 0:
                del cs[s[i - len(p)]]
        if cs == cp:
            ans.append(i - len(p) + 1) # append the start index
    return ans
```
Maintain a window of len(p) in s, and slide to right until finish. `cs == cp` is regarding to check ==/!=, which is `O(n)` time.

We first count the character appearance in `p`. For example,

```
s = "cbaebabacd"
p = "abc"
```
We get `cp = Counter({'a': 1, 'c': 1, 'b': 1})`.

And we create a Counter for `s`. We visit the string `s`, and plus 1 to build the `cs`.

`s[i - len(p)]` is the boundary in the window of length `p`. You will see for every `i >= len(p)`, you get:

```
s[i - len(p)] = c
s[i - len(p)] = b
s[i - len(p)] = a
s[i - len(p)] = e
s[i - len(p)] = b
s[i - len(p)] = a
s[i - len(p)] = b
```
with every round.

So if `s[i - len(p)]` shows in `cs`, we delete 1 in the `cs`. Finally, we compare if `cs` equals to `cp`.

### 5.
A linear time O(n) solution would be like:

``` python
def findAnagrams(self, s, p):
    l = []
    cp = collections.Counter(p)
    count = len(p)
    for i in xrange(len(s)):
        if cp[s[i]] >= 1:
            count -= 1
        cp[s[i]] -= 1

        if i >= len(p):
            if cp[s[i-len(p)]] >= 0:
                count +=1
            cp[s[i-len(p)]] += 1

        if count == 0:
            l.append(i-len(p)+1)
    return l
```
We have only one Counter for `cp`. We visit the string `s`, if the character in `s` appears in `cp`, we delete 1 to the `count`, and the `count` is the length of `p`.

``` python
    if i >= len(p):
        if cp[s[i-len(p)]] >= 0:
            count +=1
        cp[s[i-len(p)]] += 1
```
We see if every round of `s[i-len(p)` shows in `cp`, if yes, we add 1 to the `count`. We finally check if the `count` equals to `0`, meaning that if `cp == cs` as well.

