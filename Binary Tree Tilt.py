from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def set_left_right_sum(root: Optional[TreeNode]) -> int:
            if root:
                root.left_sum = set_left_right_sum(root.left)
                root.right_sum = set_left_right_sum(root.right)
                return root.left_sum + root.right_sum + root.val
            else:
                return 0

        self.res = 0
        def set_subs(root: Optional[TreeNode]):
            if root:
                self.res += abs(root.left_sum - root.right_sum)
                set_subs(root.left)
                set_subs(root.right)
        
        set_left_right_sum(root)
        set_subs(root)

        return self.res

