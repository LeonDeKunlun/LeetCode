class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stdin = input.split('\n')

        depth_len = {0: 0}
        longest_len = 0
        for line in stdin:
            line_len = len(line.lstrip('\t'))
            depth = len(line) - line_len

            if '.' in line:
                longest_len = max(longest_len, depth_len[depth] + line_len)
            else:
                depth_len[depth+1] = depth_len[depth] + line_len + 1

        return longest_len
