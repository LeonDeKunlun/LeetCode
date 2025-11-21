from bisect import bisect
from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_indices = defaultdict(list)
        for i, char in enumerate(s):
            char_indices[char].append(i)

        count = 0
        for side_indices in char_indices.values():
            if len(side_indices) < 2:
                continue
            for mid_indices in char_indices.values():
                index = bisect(mid_indices, side_indices[0])
                if index < len(mid_indices) and mid_indices[index] < side_indices[-1]:
                    count += 1
        return count