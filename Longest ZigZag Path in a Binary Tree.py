from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def do_rec(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return 0, 0
            if root.left:
                rec_left = do_rec(root.left)
                res_left = 1 + rec_left[1]
            else:
                res_left = 0
            if root.right:
                rec_right = do_rec(root.right)
                res_right = 1 + rec_right[0]
            else:
                res_right = 0
            self.res = max([self.res, res_left, res_right])
            return (res_left, res_right)
        do_rec(root)
        return self.res