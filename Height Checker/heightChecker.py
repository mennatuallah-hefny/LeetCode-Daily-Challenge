class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        out = 0
        for o, e in zip(heights, sorted(heights)):
            if o != e:
                out+=1
        return out
    


sol = Solution()
# Example 1
heights = [1,1,4,2,1,3] # Output: 3
print(sol.heightChecker(heights))

# Example 2
heights = [5,1,2,3,4] # Output: 5
print(sol.heightChecker(heights))

# Example 3
heights = [1,2,3,4,5] # Output: 0
print(sol.heightChecker(heights))
