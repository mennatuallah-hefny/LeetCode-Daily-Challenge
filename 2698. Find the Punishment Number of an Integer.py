"""
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
"""

class Solution(object):
    def can_partition(self, string_num, target):
        # Valid Partition Found
        if not string_num and target == 0:
            return True

        # Invalid Partition Found
        if target < 0:
            return False

        # Recursively check all partitions for a valid partition
        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1 :]
            left_num = int(left)

            if self.can_partition(right, target - left_num):
                return True

        return False

    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        punishment_num = 0

        # Iterate through numbers in range [1, n]
        for current_num in range(1, n + 1):
            square_num = current_num * current_num

            # Check if valid partition can be found and add squared number if so
            if self.can_partition(str(square_num), current_num):
                punishment_num += square_num

        return punishment_num
        


sol = Solution()
# Example 1: Output: 182
n = 10

print(sol.punishmentNumber(n=n))

# Example 2: Output: 1478
n = 37

print(sol.punishmentNumber(n=n))