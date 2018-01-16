class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        lastof = {}
        start = 0
        count = 0
        for end in range(len(s)):
            # move end pointer
            char = s[end]
            if char not in lastof or lastof[char] < start:
                count += 1
            lastof[char] = max(lastof.get(char, 0), end)
            # move start pointer
            while count > k:
                # check if this move make some num out of sequence
                if lastof[s[start]] == start:
                    count -= 1
                # move the start point whatever
                start += 1
            ans = max(ans, end - start + 1)
        return ans
