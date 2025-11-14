class Solution:
    def findMin(self, nums: list[int]) -> int:
        l_index = 0
        r_index = len(nums) - 1
        while l_index < r_index:
            m_index = (l_index + r_index) >> 1
            if nums[m_index] > nums[r_index]:
                l_index = m_index + 1
            else:
                r_index = m_index
        return nums[r_index]