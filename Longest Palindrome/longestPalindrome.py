from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_freq = Counter(s)

        odd_freq = False
        longest_palindrome = 0
        for value in char_freq.values():
            if value % 2 == 0:
                longest_palindrome += value
            else:
                longest_palindrome += value - 1
                odd_freq = True

        if odd_freq:
            longest_palindrome += 1

        return longest_palindrome

sol = Solution()

# Example 1
s = "abccccdd"

print(sol.longestPalindrome(s))

# Example 2
s = "a"
print(sol.longestPalindrome(s))