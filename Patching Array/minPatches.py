class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ans, nsum = 0, 0
        nums.append(n+1)
        for i in nums:
            num = min(i,n+1)
            while nsum + 1 < num:
                nsum += nsum + 1
                ans += 1
            nsum += num
        return ans