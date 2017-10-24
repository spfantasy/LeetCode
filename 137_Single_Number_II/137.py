class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we use each binary digit to count how many times it has appeared
        # if we only have one counter, then 3 is the same as 1
        # e.g. 3->ans = 011 ; 3->3->3->ans = 011->000->011
        # if we have n counters, we could hold upmost 2^n cases
        # 3->3->3->ans = 011->000->011
        #                000->011->011
        d1 = d2 = 0
        for num in nums:
            # for each digit, we want 00->01->10->00
            
            # which digit change from 01 to 00 because of num, we want it to be 10
            explode = (d1 & ~(d1 ^ num))
            d1 = d1 ^ num
            d2 = d2 ^ explode
            # which digit get 11, we want it to be 00
            explode = d1 & d2
            d1 = d1 - explode
            d2 = d2 - explode
        return d1 - d2