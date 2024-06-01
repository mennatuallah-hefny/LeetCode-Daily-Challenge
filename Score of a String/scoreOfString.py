class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Get ASCII for each character
        ascii_l = [ord(c) for c in s]
        
        # Calculate the sum of Absolute difference between char & char+1
        sum_abs_diff = 0
        for i in range(len(ascii_l) - 1):
            sum_abs_diff += abs(ascii_l[i] - ascii_l[i+1])

        return sum_abs_diff


sol = Solution()
r = sol.scoreOfString("zaz")
print(r)

