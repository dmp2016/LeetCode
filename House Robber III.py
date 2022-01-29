from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if root.__dict__.get('opt'):
            return root.__dict__.get('opt')
        opt1 = root.val
        if root.left:
            opt1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            opt1 += self.rob(root.right.left) + self.rob(root.right.right)
        opt2 = self.rob(root.left) + self.rob(root.right)

        root.opt = max(opt1, opt2)
        return max(opt1, opt2)
