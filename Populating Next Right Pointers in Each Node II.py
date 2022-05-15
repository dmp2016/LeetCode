
# Definition for a Node.
from atexit import register


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def get_next_row(node: Node):
            while node:
                if node.left:
                    yield node.left
                if node.right:
                    yield node.right
                node = node.next

        first_node = root
        while first_node:
            new_first = None
            prev = None
            for row_node in get_next_row(first_node):
                if not new_first:
                    new_first = row_node
                if prev:
                    prev.next = row_node
                prev = row_node
            first_node = new_first
        return root
