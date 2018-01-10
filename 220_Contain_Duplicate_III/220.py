class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        ids = sorted(range(len(nums)), key=lambda x: nums[x])
        for i in range(len(ids) - 1):
            j = i + 1
            while j < len(ids) and t >= nums[ids[j]] - nums[ids[i]]:
                if abs(ids[i] - ids[j]) <= k:
                    return True
                j += 1
        return False


A = Solution()
A.containsNearbyAlmostDuplicate([1, 2], 0, 1)
