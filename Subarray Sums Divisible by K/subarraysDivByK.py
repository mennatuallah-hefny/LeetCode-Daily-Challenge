class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        count = 0
        mp = {}
        mp[0] = 1  # always one prefix sum that is initially 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k  # Calculate the remainders of current sum

            if rem < 0:  # Handle negative remainders to ensure they are positive
                rem = k + rem

            if rem in mp:  # If remainder has seen before, it means there are subarrays
                count += mp[rem]  # which sum to multiple of k. Add the count of occurrences

            if rem in mp:
                mp[rem] += 1  # Increment the count for this remainder in the map
            else:
                mp[rem] = 1

        return count
        