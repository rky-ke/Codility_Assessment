# String Transformation Problem

## Problem Statement:

A string S consisting of the letters A, B, C, and D is given. The string can be transformed either by removing a letter A together with an adjacent letter B, or by removing a letter C together with an adjacent letter D.

Write a function:

```python
def solution(S)
   pass
```

that, given a string S consisting of N characters, returns any string that:
* can be obtained from S by repeatedly applying the described transformation, and
* cannot be further transformed.
If at some point there is more than one possible way to transform the string, any of the valid transformations may be chosen.

## Examples:
Given S = "CBACD", the function may return "C", because one of the possible sequences of operations is as follows:
```CBACD -> CBA -> C```
Given S = "CABABD" the function may return an empty string, because one possible sequence of operations is:
```CABABD -> CABD -> CD```

Given string S = "ACBDACBD" the function should return "ACBDACBD", because no operation can be applied to string S.

## Requirements:
Write an efficient algorithm for the following assumptions:

* The length of string S is within the range [0..250,000].
* String S is made only of the following characters: 'A', 'B', 'C', and/or 'D'.