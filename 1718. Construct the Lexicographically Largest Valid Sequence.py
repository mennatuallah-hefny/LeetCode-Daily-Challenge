"""
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, 

sequence a has a number greater than the corresponding number in b. 

For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, 

and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
"""

class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (2 * n - 1)  # Initialize the result list
        used = [False] * (n + 1)     # To track used numbers

        def backtrack(index):
            if index == len(result):
                return True  # Successfully filled the sequence

            if result[index] != 0:
                return backtrack(index + 1)  # Skip if already filled

            # Try to place numbers from n down to 1
            for num in range(n, 0, -1):
                if not used[num]:
                    if num == 1:
                        result[index] = num
                        used[num] = True
                    else:
                        next_index = index + num  # The position for the second occurrence
                        if next_index < len(result) and result[next_index] == 0:
                            # Place the number
                            result[index] = num
                            result[next_index] = num
                            used[num] = True
                        else:
                            continue  # Skip if cannot place the second occurrence

                    # Recur to fill the next position
                    if backtrack(index + 1):
                        return True  # Found a valid sequence

                    # Backtrack
                    result[index] = 0
                    if num == 1:
                        used[num] = False
                    else:
                        result[next_index] = 0
                        used[num] = False

            return False  # No valid placement found

        backtrack(0)  # Start backtracking from index 0
        return result
        


sol = Solution()
# Example 1: Output: [3,1,2,3,2]
n = 3

print(sol.constructDistancedSequence(n=n))

# Example 2: Output: [5,3,1,4,3,5,2,4,2]
n = 5

print(sol.constructDistancedSequence(n=n))