import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def do_from_left(node: TreeNode):
            if node is None:
                return []
            for item in do_from_left(node.left):
                yield item
            yield node
            for item in do_from_left(node.right):
                yield item

        def do_from_right(node: TreeNode):
            if node is None:
                return []
            for item in do_from_right(node.right):
                yield item
            yield node
            for item in do_from_right(node.left):
                yield item

        item1 = None
        prev_item = None
        prev_val = -math.inf
        for item in do_from_left(root):
            if prev_val > item.val:
                item1 = prev_item
                break
            prev_item = item
            prev_val = item.val

        
        item2 = None
        prev_item = None
        prev_val = math.inf
        for item in do_from_right(root):
            if prev_val < item.val:
                item2 = prev_item
                break
            prev_item = item
            prev_val = item.val
        
        item1.val, item2.val = item2.val, item1.val
