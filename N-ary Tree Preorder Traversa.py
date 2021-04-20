from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []        
        def do_rec(root: Node) -> None:
            if not root:
                return
            res.append(root.val)
            for node in root.children:
                do_rec(node)

        do_rec(root)
        return res

