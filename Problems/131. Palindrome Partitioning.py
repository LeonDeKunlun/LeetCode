from collections import defaultdict, deque

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return []

        s_len = len(s)
        palindromes = defaultdict(deque)

        def palindrome_backtrack(start, end):
            if 0 <= start and end < s_len and s[start] == s[end]:
                palindromes[start].append(end)
                palindrome_backtrack(start-1, end+1)

        for i in range(s_len):
            palindrome_backtrack(i, i)
            palindrome_backtrack(i, i+1)

        results = list()

        def partition_backtrack(partition, start):
            if start == s_len:
                results.append(list(partition))
                return

            for end in palindromes[start]:
                partition.append(s[start : end+1])
                partition_backtrack(partition, end+1)
                partition.pop()

        partition_backtrack(deque(), 0)
        return results
