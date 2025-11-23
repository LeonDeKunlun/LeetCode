from math import inf

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        sum_r = num_sum % 3
        if sum_r == 0:
            return num_sum

        mod_min = [[inf] * 2 for _ in range(3)]
        for num in nums:
            if (r := num % 3) > 0:
                if num < mod_min[r][0]:
                    *mod_min[r], _ = num, *mod_min[r]
                elif num < mod_min[r][1]:
                    mod_min[r][1] = num
        return num_sum - min(mod_min[sum_r][0], sum(mod_min[sum_r ^ 3]))