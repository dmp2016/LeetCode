from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res_nodes = [root]
        while True:
            new_res_nodes = []
            for item in res_nodes:
                if isinstance(item, TreeNode):
                    if item.left:
                        new_res_nodes.append(item.left)
                    new_res_nodes.append(item.val)
                    if item.right:
                        new_res_nodes.append(item.right)
                else:
                    new_res_nodes.append(item)
            if len(new_res_nodes) == len(res_nodes):
                break
            res_nodes = new_res_nodes
        return [item.val for item in res_nodes]
