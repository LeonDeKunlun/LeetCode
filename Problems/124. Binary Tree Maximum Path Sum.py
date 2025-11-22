from math import inf

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def path_sums(root):
            if root is None:
                return (-inf, -inf)
            left, right = path_sums(root.left), path_sums(root.right)
            root_end_path = max(left[0], right[0], 0) + root.val
            root_path = max(left[0], 0) + root.val + max(right[0], 0)
            max_path = max(root_path, left[1], right[1])
            return (root_end_path, max_path)
        return max(path_sums(root))