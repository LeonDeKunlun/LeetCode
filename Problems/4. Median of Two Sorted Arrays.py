from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        half_len = (m + n) // 2
        l_idx, r_idx = max(0, half_len - n), min(m, half_len)
        while l_idx < r_idx:
            # split nums_i into [: idx_i] and [idx_i :]
            idx_1 = (l_idx + r_idx) >> 1
            idx_2 = half_len - idx_1
            if idx_1 < m and idx_2 > 0 and nums2[idx_2-1] > nums1[idx_1]:
                l_idx = idx_1 + 1
            else:
                r_idx = idx_1
        idx_1, idx_2 = l_idx, half_len - l_idx
        r_median = min(nums1[idx_1] if idx_1 < m else inf, nums2[idx_2] if idx_2 < n else inf)
        if (m + n) & 1 == 1:
            return float(r_median)
        l_median = max(nums1[idx_1-1] if idx_1 > 0 else -inf, nums2[idx_2-1] if idx_2 > 0 else -inf)
        return (l_median + r_median) * 0.5