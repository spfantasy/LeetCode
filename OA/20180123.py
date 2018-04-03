class Solution(object):
    def func(self, nums):
        withLast = [None] * len(nums)
        withoutLast = [None] * len(nums)
        for i in range(len(nums)):
            if i - 1 >= 0:
                withLast[i] = max(
                    withLast[i - 1], withoutLast[i - 1]) + nums[i]
                withoutLast[i] = withLast[i - 1]
            else:
                withLast[i] = nums[i]
                withoutLast[i] = 0
        return max(withLast[-1], withoutLast[-1])


S = Solution()
print(S.func([9, -1, -3, 4, 5]))
