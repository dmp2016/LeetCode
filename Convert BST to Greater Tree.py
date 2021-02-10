# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def do(self, node: TreeNode, d: int) -> int:
        if node is not None:
            r = self.do(node.right)
            res = r + self.do(node.left, node.val + r) + node.val
            node.val += r + d
            return res
        else:
            return 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.do(root, 0)
        return root
