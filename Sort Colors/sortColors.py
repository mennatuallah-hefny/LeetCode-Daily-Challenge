class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1

        for i in range(n):
            if i < zeros:
                nums[i] = 0
            elif zeros <= i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2
        
        return nums