from itertools import accumulate

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        x = accumulate(nums, lambda num1, num2: r if (r := 2*num1 + num2) < 5 else r-5)
        answer = [xi == 0 for xi in x]
        return answer