class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = (left + right) >> 1
            if (mid + 1) * (mid + 1) <= x:
                left = mid + 1
            else: # if x < (mid + 1) * (mid + 1)
                right = mid
        return left
