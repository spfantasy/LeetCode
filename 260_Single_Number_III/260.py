class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        # get xor of two single numbers
        for num in nums:
        	total ^= num
        # get the last digit with '1'
        # which is the last digit that num1 and num2 are different from each other
        # a&(a-1) mark digit of last '1' and after with '0'
        # (a&(a-1))^a captures '1' in the above part
        lastbit = (total & (total - 1)) ^ total
        num1 = 0
        num2 = 0
        #xor by making two groups depending on last digit
        for num in nums:
        	if num & lastbit:
        		num1 ^= num
        	else:
        		num2 ^= num
        return [num1, num2]