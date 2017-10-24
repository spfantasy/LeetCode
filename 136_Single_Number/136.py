class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = b00000000
        # -> num = 5
        # ans = b00000101
        # -> num = 3
        # ans = b00000110
        # -> num = 3
        # ans = b00000101
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans