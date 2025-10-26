# from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # return bisect_left(nums, target)

        l_index = 0
        r_index = len(nums)
        while l_index < r_index:
            m_index = (l_index + r_index) >> 1
            m = nums[m_index]
            if target <= m:
                r_index = m_index
            elif m < target:
                l_index = m_index + 1

        return r_index
