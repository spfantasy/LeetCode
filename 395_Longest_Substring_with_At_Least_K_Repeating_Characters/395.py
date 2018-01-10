class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        splitter = " "
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(_s, k) for _s in s.split(char))
        return len(s)
