"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) 

such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
"""

from collections import defaultdict
from itertools import combinations


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_count = defaultdict(int)
    
        # Generate all possible products of pairs
        for a, b in combinations(nums, 2):
            product_count[a * b] += 1
        
        # Calculate the number of valid tuples
        result = 0
        for count in product_count.values():
            if count >= 2:
                result += count * (count - 1) * 4
        
        return result
        

sol = Solution()
# Example 1: Output: 8
nums = [2,3,4,6]

print(sol.tupleSameProduct(nums=nums))

# Example 2: Output: 16
nums = [1,2,4,5,10]

print(sol.tupleSameProduct(nums=nums))