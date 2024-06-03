class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        first_ptr = longest_prefix = 0

        while first_ptr < len(s) and longest_prefix < len(t):
            if s[first_ptr] == t[longest_prefix]:
                longest_prefix += 1
            first_ptr += 1

        min_num_char = len(t) - longest_prefix
        return  min_num_char
