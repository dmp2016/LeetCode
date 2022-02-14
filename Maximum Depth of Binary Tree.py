from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root: Optional[TreeNode], level: int) -> None:
            self.res = max(self.res, level)
            if root:
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        
        dfs(root, 0)
        return self.res
