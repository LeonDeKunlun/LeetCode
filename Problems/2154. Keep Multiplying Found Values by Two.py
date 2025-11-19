class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original <<= 1
        return original