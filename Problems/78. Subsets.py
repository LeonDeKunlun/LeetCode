from collections import deque
from itertools import islice

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = list()

        def backtrack(path, start):
            results.append(list(path))

            for i, num in islice(enumerate(nums), start, None):
                path.append(num)
                backtrack(path, i+1)
                path.pop()

        backtrack(deque(), 0)
        return results
