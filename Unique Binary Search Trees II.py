from typing import List, Optional
from pprint import pprint


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def build(a: int, b: int):
            res = []
            for m in range(a, b + 1):
                left_trees = build(a, m - 1)
                right_trees = build(m + 1, b)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(m, left_tree, right_tree)
                        res.append(node)
            return res if res else [None]
        
        return build(1, n)

test = Solution()
t = test.generateTrees(2)
pprint(t)
