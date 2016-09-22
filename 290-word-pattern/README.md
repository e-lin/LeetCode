290. Word Pattern
---

- Total Accepted: 52275
- Total Submissions: 168170
- Difficulty: Easy


Problem
---
Given a `pattern` and a string `str`, find if `str` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `str`.

**Examples:**

1. pattern = `"abba"`, str = `"dog cat cat dog"` should return true.
2. pattern = `"abba"`, str = `"dog cat cat fish"` should return false.
3. pattern = `"aaaa"`, str = `"dog cat cat dog"` should return false.
4. pattern = `"abba"`, str = `"dog dog dog dog"` should return false.

**Notes:**

You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters separated by a single space.

```
pattern = "he"
str = "unit"
```
are expected `False`.

```
pattern = "ab"
str = "b c"
```
are expected `True`.
