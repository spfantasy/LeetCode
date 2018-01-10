class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # based on LIS method
        if len(nums) < 3:
            return False
        LengthToEnding = [nums[0]]
        for num in nums:
            for i in range(len(LengthToEnding))[::-1]:
                if num > LengthToEnding[i]:
                    if i == len(LengthToEnding) - 1:
                        LengthToEnding.append(num)
                    else:
                        LengthToEnding[i+1] = min(LengthToEnding[i+1],num)
                else:
                    LengthToEnding[0] = min(LengthToEnding[0],num)
            if len(LengthToEnding) == 3:
                return True
        return False