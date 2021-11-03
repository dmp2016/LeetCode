from typing import Counter, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            self.cur = 0
            self.res = 0

            def dfs(root: TreeNode) -> None:
                self.cur = self.cur * 10 + root.val
                if not root.left and not root.right:
                    self.res += self.cur
                else:
                    if root.left:
                        dfs(root.left)
                    if root.right:
                        dfs(root.right)
                self.cur //= 10

            dfs(root)
            return self.res