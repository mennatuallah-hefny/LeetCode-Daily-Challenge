from collections import Counter


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_chars_freq = Counter(words[0])
        for word in words:
            common_chars_freq &= Counter(word)
        
        return list(common_chars_freq.elements())
    
words = ["bella","label","roller"]
sol = Solution()
print(sol.commonChars(words))
