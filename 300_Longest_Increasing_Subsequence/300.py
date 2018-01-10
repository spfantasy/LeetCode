class Solution:
    def BinarySearch(self, vector, num):
        # find the maximum number(index) in vector which is smaller than num
        if len(vector) == 0 or vector[0] >= num:
            return -1
        start = 0
        end = len(vector) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if vector[mid] < num:
                start = mid
            else:
                end = mid
        if vector[end] < num:
            return end
        elif vector[start] < num:
            return start
        else:
            raise KeyError

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LengthToTail = []  # LengthToTail[i] -> minimum ending that has length i+1
        # OPT = [None]*len(nums)
        for num in nums:
            ValidLengthAccToTail = self.BinarySearch(LengthToTail, num) + 1

            if ValidLengthAccToTail >= len(LengthToTail):
                LengthToTail.append(num)
            else:
                LengthToTail[ValidLengthAccToTail] = min(
                    LengthToTail[ValidLengthAccToTail], num)
        return len(LengthToTail)
