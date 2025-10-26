from collections import deque
from itertools import islice

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        results = list()

        def backtrack(comb, remain, start):
            if remain == 0:
                results.append(list(comb))
                return

            for i, candidate in islice(enumerate(candidates), start, None):
                if candidate > remain:
                    break
                comb.append(candidate)
                backtrack(comb, remain - candidate, i)
                comb.pop()

        backtrack(deque(), target, 0)

        return results
