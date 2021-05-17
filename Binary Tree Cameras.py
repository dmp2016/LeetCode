# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        def do_rec1(parent: TreeNode, cur: TreeNode) -> None:
            cur.val = 2
            if cur.left:
                do_rec1(cur, cur.left)
            if cur.right:
                do_rec1(cur, cur.right)

            if (not cur.left or cur.left.val == 2) and (not cur.right or cur.right.val == 2) and cur.val != 1:
                if parent:
                    parent.val = 1
                else:
                    cur.val = 1

        def do_rec2(cur: TreeNode) -> None:
            if cur:
                return (1 if cur.val == 1 else 0) + do_rec2(cur.left) + do_rec2(cur.right)
            else:
                return 0

        do_rec1(None, root)
        return do_rec2(root)
