from typing import List
from collections import defaultdict


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        xc = defaultdict(list)

        def go(node: TreeNode, cur_x: int, cur_y: int):
            if node:
                xc[cur_x].append((cur_y, node.val))
                go(node.left, cur_x - 1, cur_y + 1)
                go(node.right, cur_x + 1, cur_y + 1)

        go(root, 0, 0)
        res = []
        for key in sorted(xc.keys()):
            res.append([a for _, a in sorted(xc[key])])
        return res

