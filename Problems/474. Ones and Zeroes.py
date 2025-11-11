from collections import Counter

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dynamic_max_form = {(0, 0): 0}
        for binary in strs:
            cnt = Counter(binary)
            new_max_form = dict()
            for (i, j), max_form in dynamic_max_form.items():
                i += cnt['0']
                j += cnt['1']
                coord = (i, j)
                if i <= m and j <= n and dynamic_max_form.get(coord, 0) <= max_form:
                    new_max_form[coord] = max_form + 1
            dynamic_max_form.update(new_max_form)
        return max(dynamic_max_form.values())
