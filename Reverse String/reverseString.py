class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return [c for c in reversed(s)]    
    
sol = Solution()

# Example one 
s = ["h","e","l","l","o"]

print(sol.reverseString(s))

# Example two
s = ["H","a","n","n","a","h"]
print(sol.reverseString(s))
