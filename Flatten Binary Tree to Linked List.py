# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def do_rec(root: TreeNode) -> TreeNode:
            if not root:
                return None
            left = root.left
            right = root.right
            root.left = None
            if left:
                left_end = do_rec(left)
                root.right = left
                root = left_end
            if right:
                right_end = do_rec(right)
                root.right = right
                root = right_end
            return root
            
        do_rec(root)