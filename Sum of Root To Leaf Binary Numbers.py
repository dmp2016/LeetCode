from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.cur = 0
        self.res = 0
        def do_rec(root: Optional[TreeNode]):
            if root:
                self.cur <<= 1
                self.cur += root.val
                if root.left:
                    do_rec(root.left)
                if root.right:
                    do_rec(root.right)
                if not (root.left or root.right):
                    self.res += self.cur
                self.cur >>= 1
        
        do_rec(root)
        return self.res
