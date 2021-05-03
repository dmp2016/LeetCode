from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack_node = [root]
        stack_stat = [0]
        res = []

        while stack_node:
            if stack_stat[-1] == 2:
                stack_node.pop()
                stack_stat.pop()
            elif stack_stat[-1] == 1:
                stack_stat[-1] += 1
                if stack_node[-1].right:
                    stack_node.append(stack_node[-1].right)
                    stack_stat.append(0)
            elif stack_stat[-1] == 0:
                res.append(stack_node[-1].val)
                stack_stat[-1] += 1
                if stack_node[-1].left:
                    stack_node.append(stack_node[-1].left)
                    stack_stat.append(0)
        return res
