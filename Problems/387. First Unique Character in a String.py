from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        exist = dict()
        exist_rep = set()
        ordered_chars = deque()
        for i, char in enumerate(s):
            if char not in exist:
                ordered_chars.append(char)
                exist[char] = i
            elif char not in exist_rep:
                exist_rep.add(char)
                if len(exist_rep) == 26:
                    return -1
        if len(exist) == len(exist_rep):
            return -1
        for char in ordered_chars:
            if char not in exist_rep:
                return exist[char]
