from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0

        def do_rec(root):
            res = 0
            if root:
                if low <= root.val <= high:
                    res += root.val
                res += do_rec(root.left) + do_rec(root.right)
            return res

        return do_rec(root)
