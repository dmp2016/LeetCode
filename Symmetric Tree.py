from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def rec(nodes1: List[TreeNode], nodes2: List[TreeNode]) -> bool:
            if list(map(lambda x: x.val if x else None, nodes1)) != list(map(lambda x: x.val if x else None, nodes2))[::-1]:
                return False

            new_nodes1 = []
            for item in nodes1:
                if item:
                    new_nodes1.append(item.left)
                    new_nodes1.append(item.right)
            new_nodes2 = []
            for item in nodes2:
                if item:
                    new_nodes2.append(item.left)
                    new_nodes2.append(item.right)
            if not new_nodes1 and not new_nodes2:
                return True
            else:
                return rec(new_nodes1, new_nodes2)

        return rec([root.left], [root.right])
