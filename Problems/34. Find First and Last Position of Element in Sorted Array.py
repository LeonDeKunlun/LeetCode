class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        l_index = 0
        r_index = len(nums)-1
        while l_index <= r_index:
            m_index = (l_index + r_index) >> 1
            m = nums[m_index]
            if m == target and (m_index == 0 or nums[m_index-1] < target):
                start = m_index
                break
            elif m < target:
                l_index = m_index + 1
            else:
                r_index = m_index - 1
        if start == -1:
            return [-1, -1]

        l_index = start
        r_index = len(nums)-1
        while l_index < r_index:
            m_index = (l_index + r_index + 1) >> 1
            if nums[m_index] == target:
                l_index = m_index
            else:
                r_index = m_index - 1
        return [start, r_index]
