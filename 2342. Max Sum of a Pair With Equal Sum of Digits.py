"""
You are given a 0-indexed array nums consisting of positive integers. 

You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
"""

class Solution(object):

    def get_digits_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_for_digit_sum = {}
    
        # This will store the best (maximum) pair sum found.
        best_sum = -1
        
        for num in nums:
            # Calculate the digit sum of the current number.
            dsum = self.get_digits_sum(num)
            
            # If we have already seen a number with the same digit sum,
            # then we can form a pair with the current number.
            if dsum in max_for_digit_sum:
                # Update the best_sum with the sum of the current number and
                # the largest number seen so far with the same digit sum.
                best_sum = max(best_sum, max_for_digit_sum[dsum] + num)
                # Also update the maximum number for this digit sum if needed.
                max_for_digit_sum[dsum] = max(max_for_digit_sum[dsum], num)
            else:
                # If no number with this digit sum has been seen, add it to the map.
                max_for_digit_sum[dsum] = num

        return best_sum


sol = Solution()
# Example 1: Output: 54
nums = [18,43,36,13,7]

print(sol.maximumSum(nums=nums))

# Example 2: Output: -1
nums = [10,12,19,14]

print(sol.maximumSum(nums=nums))