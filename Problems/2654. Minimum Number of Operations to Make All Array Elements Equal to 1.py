from functools import reduce
from itertools import pairwise
from math import gcd

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if (cnt_1 := nums.count(1)) > 0:
            return len(nums) - cnt_1
        if reduce(gcd, nums) != 1:
            return -1
        gcds = nums.copy()
        operation = -1
        while len(gcds) > 1:
            gcds = [gcd(*pair) for pair in pairwise(gcds)]
            if any(divisor == 1 for divisor in gcds):
                operation = 2 * len(nums) - len(gcds) - 1
                break
        return operation
