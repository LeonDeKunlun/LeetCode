class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_one = -(k+1)
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one <= k:
                    return False
                last_one = i
        return True