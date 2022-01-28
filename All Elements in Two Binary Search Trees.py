from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def get_vals(root: TreeNode) -> List[int]:
            if not root:
                yield from []
            else:
                yield root.val
                for d in get_vals(root.left):
                    yield d
                for d in get_vals(root.right):
                    yield d

        return sorted(list(get_vals(root1)) + list(get_vals(root2)))
        

class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        q = deque([root1, root2])
        res = []
        while q:
            v = q.pop()
            if v:
                res.append(v.val)
                q.append(v.left)
                q.append(v.right)
        return sorted(res)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        q = deque([root1, root2])
        res = []
        while q:
            v = q.pop()
            if v:
                res.append(v.val)
                q.append(v.left)
                q.append(v.right)
        return sorted(res)

