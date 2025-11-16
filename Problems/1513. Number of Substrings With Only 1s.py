from functools import cache

class Solution:
    def numSub(self, s: str) -> int:
        @cache
        def sum_n(n):
            return n * (n+1) >> 1

        return sum(sum_n(len(ones)) for ones in s.split('0')) % 1_000_000_007