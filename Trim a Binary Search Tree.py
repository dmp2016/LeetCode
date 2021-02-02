# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def check_node(node: TreeNode) -> TreeNode:
            if node:
                if node.val < low:
                    node = check_node(node.right)
                elif node.val > high:
                    node = check_node(node.left)
                if node:
                    node.left = check_node(node.left)
                    node.right = check_node(node.right)
            return node

        return check_node(root)
