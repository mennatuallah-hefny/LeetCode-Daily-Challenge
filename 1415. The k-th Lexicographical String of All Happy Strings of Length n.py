"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. 

You will find the 9th string = "cab"
"""

class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.k = k  
        self.answer = ""  
    
        # The backtracking function that builds happy strings recursively
        def backtrack(current):
            # Base case: if current string is of length n, it's a complete happy string.
            if len(current) == n:
                self.k -= 1  # We found one more happy string.
                if self.k == 0:
                    self.answer = current  # Found the k-th happy string.
                return
            
            # Iterate over letters in lexicographical order
            for char in ['a', 'b', 'c']:
                # Skip if the character is the same as the last one to maintain the happy string property.
                if current and current[-1] == char:
                    continue
                
                # If answer is already found, no need to continue further.
                if self.answer:
                    return
                
                # Append the current letter and continue backtracking.
                backtrack(current + char)
        
        # Start backtracking with an empty string.
        backtrack("")
        return self.answer  # Return the result

sol = Solution()
# Example 1: Output: "c"
n = 1
k = 3

print(sol.getHappyString(n=n, k=k))

# Example 2: Output: ""
n = 1
k = 4

print(sol.getHappyString(n=n, k=k))

# Example 3: Output: "cab"
n = 3
k = 9

print(sol.getHappyString(n=n, k=k))