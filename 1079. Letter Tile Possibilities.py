"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
"""

from typing import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # Count the frequency of each letter.
        counter = Counter(tiles)
        self.result = 0
        
        def backtrack(counter):
            # Try to use each letter that is still available.
            for tile in counter:
                if counter[tile] > 0:
                    # Choose the tile and increase our count.
                    self.result += 1
                    
                    # Use this tile: reduce its count.
                    counter[tile] -= 1
                    
                    # Continue building the sequence.
                    backtrack(counter)
                    
                    # Backtrack: restore the count.
                    counter[tile] += 1
        
        backtrack(counter)
        return self.result

sol = Solution()
# Example 1: Output: 8
tiles = "AAB"

print(sol.numTilePossibilities(tiles=tiles))

# Example 2: Output: 188
tiles = "AAABBC"

print(sol.numTilePossibilities(tiles=tiles))

# Example 3: Output: 1
tiles = "V"

print(sol.numTilePossibilities(tiles=tiles))