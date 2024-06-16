class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        min_increments = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                min_increments+=increment

                nums[i] = nums[i - 1] + 1

        return min_increments
    

sol = Solution()
# Example 1
nums = [1,2,2] # Out 1

print(sol.minIncrementForUnique(nums))

# Example 2

nums = [3,2,1,2,1,7] # Output: 6
print(sol.minIncrementForUnique(nums))
