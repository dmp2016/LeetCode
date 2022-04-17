from typing import Tuple, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def do_rec(root: TreeNode) -> Tuple[Optional[TreeNode]]:
            if root.left:
                lp = do_rec(root.left)
                lp[1].right = root
                root.left = None
                res0 = lp[0]
            else:
                res0 = root
            if root.right:
                rp = do_rec(root.right)
                root.right = rp[0]
                res1 = rp[1]
            else:
                res1 = root

            return res0, res1

        return do_rec(root)[0] if root else None


test = Solution()
test.increasingBST(None)