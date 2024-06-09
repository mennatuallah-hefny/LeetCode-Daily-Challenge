class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
    
        # Dictionary to store the first occurrence index of each modulo value
        mod_index = {}
        # Initialize the cumulative sum
        curr_sum = 0
        
        for i in range(len(nums)):
            # Update the cumulative sum
            curr_sum += nums[i]
            
            # Calculate the modulo of the current sum with k
            mod = curr_sum % k
            
            # If the modulo is 0 and we have at least two elements, return True
            if mod == 0 and i + 1 >= 2:
                return True
            
            # If the modulo has been seen before
            if mod in mod_index:
                # Check if the distance between the current index and the stored index is at least 2
                if i - mod_index[mod] >= 2:
                    return True
            else:
                # Store the index of the first occurrence of this modulo
                mod_index[mod] = i
        
        # If no valid subarray is found, return False
        return False