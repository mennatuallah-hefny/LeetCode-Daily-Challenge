"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
"""
# Time Limit Exceeded
# class Solution(object):
#     def maxWidthRamp(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         maximum_ramp_width = 0

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 # Check if nums[i] <= nums[j]
#                 if nums[i] <= nums[j]:
#                     # Get ramp width
#                     ramp_width = j - i
#                     # Update max ramp width
#                     maximum_ramp_width = max(maximum_ramp_width, ramp_width)

#         return maximum_ramp_width


class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        n = len(nums)
        
        # Build a decreasing stack
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        # Traverse from right to left
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width

sol = Solution()
# Example 1: Output: 4
nums = [6,0,8,2,1,5]


print(sol.maxWidthRamp(nums=nums))

# Example 2: Output: 7
nums = [9,8,1,0,1,9,4,0,4,1]

print(sol.maxWidthRamp(nums=nums))