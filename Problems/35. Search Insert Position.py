# from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # return bisect_left(nums, target)

        l_index = 0
        r_index = len(nums)
        while l_index < r_index:
            m_index = (l_index + r_index) >> 1
            if nums[m_index] < target:
                l_index = m_index + 1
            else: # if target <= nums[m_index]
                r_index = m_index
        return r_index
