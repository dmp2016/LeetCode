from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            front = [root]
            while front:
                new_front = []
                for node in front:
                    if node.left:
                        new_front.append(node.left)
                        new_front.append(node.right)
                front = new_front
                for ind in range(1, len(front)):
                    front[ind - 1].next = front[ind]
        return root
