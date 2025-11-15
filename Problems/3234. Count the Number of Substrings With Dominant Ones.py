from functools import cache
from math import floor, sqrt

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        max_zeroes = floor((sqrt(4*len(s)+1) - 1) / 2)
        ones_len = [len(ones) for ones in s.split('0')]

        @cache
        def sum_n(n):
            if n < 0:
                return 0
            return n * (n+1) >> 1

        @cache
        def squared(n):
            return n * n

        result = 0
        for i in range(len(ones_len)):
            ones_i = len_sum = ones_len[i]
            result += sum_n(ones_i)
            for j in range(i+1, min(len(ones_len), i+max_zeroes+1)):
                ones_j = ones_len[j]
                len_sum += ones_j
                zeroes = squared(j-i)
                if len_sum >= zeroes:
                    result += (ones_i+1) * (ones_j+1)
                    diff = max(0, zeroes - (len_sum - ones_i - ones_j))
                    result -= sum_n(diff)
                    result += sum_n(diff - ones_i - 1) + sum_n(diff - ones_j - 1)
        return result