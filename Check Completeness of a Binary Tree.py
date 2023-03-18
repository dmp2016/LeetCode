from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        front = [root]
        p2 = 1
        while front:
            new_front = []
            for item in front:
                new_front.append(item.left)
                new_front.append(item.right)
            while new_front and new_front[-1] is None:
                new_front.pop()
            for item in new_front:
                if item is None:
                    return False
            if new_front and len(front) != p2:
                return False
            p2 <<= 1
            front = new_front
        return True
