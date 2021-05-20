from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        front = [root]
        while front:
            res.append([])
            new_front = []
            for a in front:
                if a.left:
                    new_front.append(a.left)
                    res[-1].append(a.left.val)
                if a.right:
                    new_front.append(a.right)
                    res[-1].append(a.right.val)
            front = new_front
        res.pop()
        return res
