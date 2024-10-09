"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
"""

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_parenthesis, min_insert_req = 0, 0

        for char in s:
            if char == '(':
                open_parenthesis += 1
            else:
                if open_parenthesis > 0:
                    open_parenthesis -= 1
                else:
                    min_insert_req += 1
        return min_insert_req + open_parenthesis


sol = Solution()
# Example 1: Output: 1
s = "())"

print(sol.minAddToMakeValid(s=s))

# Example 2: Output: 3
s = "((("

print(sol.minAddToMakeValid(s=s))