# Problem Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets

class Solution(object):
    
    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        count = 0

        for day in bloomDay:
            # If the flower is bloomed, add to the set. Else reset the count.
            if day <= mid:
                count += 1
            else:
                count = 0

            if count == k:
                num_of_bouquets += 1
                count = 0

        return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = (start + end) // 2

            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays
    

sol = Solution()

# Example 1 -> Output: 3
bloomDay = [1,10,3,10,2]
m = 3
k = 1

print(sol.minDays(bloomDay, m, k))

# Example 2 -> Output: -1
bloomDay = [1,10,3,10,2]
m = 3
k = 2

print(sol.minDays(bloomDay, m, k))

# Example 3 -> Output: 12
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

print(sol.minDays(bloomDay, m, k))
