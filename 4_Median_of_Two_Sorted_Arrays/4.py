import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]  [     |     ]
        :type nums2: List[int]  [   |   ]
        :rtype: float
        """
        # median_left  = num[(n-1)//2] 4->1 4->2
        # median_right = num[n//2]     4->2 5->2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # [ 1 2 3 4 ] len = 4
        # [#########] idx 0 - 8
        start = 0
        end = 2 * len(nums1)
        while start + 1 < end:
            mid1 = start + (end - start) // 2
            mid2 = len(nums1) + len(nums2) - mid1
            L1 = nums1[(mid1 - 1) // 2] if mid1 > 0 else -sys.maxsize - 1
            L2 = nums2[(mid2 - 1) // 2] if mid2 > 0 else -sys.maxsize - 1
            R1 = nums1[mid1 // 2] if mid1 < 2 * len(nums1) else sys.maxsize
            R2 = nums2[mid2 // 2] if mid2 < 2 * len(nums2) else sys.maxsize
            if L1 > R2:
                end = mid1
            elif L2 > R1:
                start = mid1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2
        # check for the last two itms
        for mid1 in [start, end]:
            mid2 = len(nums1) + len(nums2) - mid1
            L1 = nums1[(mid1 - 1) // 2] if mid1 > 0 else -sys.maxsize - 1
            L2 = nums2[(mid2 - 1) // 2] if mid2 > 0 else -sys.maxsize - 1
            R1 = nums1[mid1 // 2] if mid1 < 2 * len(nums1) else sys.maxsize
            R2 = nums2[mid2 // 2] if mid2 < 2 * len(nums2) else sys.maxsize
            if L1 > R2:
                end = mid1
            elif L2 > R1:
                start = mid1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2
