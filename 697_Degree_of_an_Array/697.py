class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maximum = 0
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            maximum = max(maximum, count[num])
        keys = set([num for num in count if count[num] == maximum])
        count = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in keys:
                count[key] = count.get(key, [len(nums) - 1, 0])
                count[key][0] = min(count[key][0], i)
                count[key][1] = max(count[key][1], i)
        ans = len(nums)
        for key in count:
            ans = min(ans, count[key][1] - count[key][0] + 1)
        return ans
