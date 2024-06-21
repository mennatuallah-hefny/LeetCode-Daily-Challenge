class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        unrealized_customers =  0
        non_grumpy = sum([c*(1-g) for c, g in zip(customers, grumpy)])

        # Calculate initial number of unrealized customers in first 'minutes' window
        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        # Slide the 'minutes' window across the rest of the customers array
        for i in range(minutes, n):
            # Add current minute's unsatisfied customers if the owner is grumpy
            # and remove the customers that are out of the current window
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]

            # Update the maximum unrealized customers
            max_unrealized_customers = max(
                max_unrealized_customers, unrealized_customers
            )

        # total = maximum possible satisfied customers due to secret technique + customers came in non_grumpy time 
        total_customers = max_unrealized_customers + non_grumpy

        return total_customers
    


sol = Solution()

"""Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""
# Example 1 -> Output: 16

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

print(sol.maxSatisfied(customers, grumpy, minutes))

# Example 2 -> Output: 1

customers = [1]
grumpy = [0]
minutes = 1

print(sol.maxSatisfied(customers, grumpy, minutes))
