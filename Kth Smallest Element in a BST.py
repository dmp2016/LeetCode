from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def do_from_left(node: TreeNode):
            if node is None:
                return []
            for item in do_from_left(node.left):
                yield item
            yield node
            for item in do_from_left(node.right):
                yield item

        
        for i, item in enumerate(do_from_left(root)):
            if i == k - 1:
                return item.val
            
