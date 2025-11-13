from itertools import accumulate
import re

class Solution:
    def maxOperations(self, s: str) -> int:
        ones_list = re.findall(r'(1+)0', s)
        operation = sum(accumulate(map(len, ones_list)))
        return operation
