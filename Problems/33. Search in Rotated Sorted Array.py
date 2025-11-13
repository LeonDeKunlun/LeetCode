class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l_index = 0
        r_index = len(nums)-1
        while l_index <= r_index:
            m_index = (l_index + r_index) >> 1
            l = nums[l_index]
            m = nums[m_index]
            if m == target:
                return m_index
            if (l <= m) ^ (l <= target) ^ (target < m):
                r_index = m_index - 1
            else:
                l_index = m_index + 1
        return -1
