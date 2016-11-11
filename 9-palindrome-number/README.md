9. Palindrome Number
---

- Total Accepted: 147079
- Total Submissions: 444764
- Difficulty: Easy


Problem
---
Determine whether an integer is a palindrome. Do this without extra space.


[Remove all whitespace in a string][R1]
---
If you want to remove leading and ending spaces, use `str.strip()`:

``` python
sentence = ' hello  apple'
sentence.strip()
>>> 'hello  apple'
```

If you want to remove all spaces, use `str.replace()`:

``` python
sentence = ' hello  apple'
sentence.replace(" ", "")
>>> 'helloapple'
```

If you want to remove duplicated spaces, use `str.split()`:

``` python
sentence = ' hello  apple'
" ".join(sentence.split())
>>> 'hello apple'
```


Spoilers...
---
**Some hints:**

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


Related Challenges
---
- `5. Longest Palindromic Substring`
- `409. Longest Palindrome`
- `125. Valid Palindrome`
- `234. Palindrome Linked List`
- `131. Palindrome Partitioning` (M)


[R1]: http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string