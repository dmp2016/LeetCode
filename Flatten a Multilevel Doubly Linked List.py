from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def process_node(head: Node) -> Optional[Node]:
            tail = None
            while head:
                if head.child:
                    old_next = head.next
                    head.next = head.child
                    head.child.prev = head
                    new_head = process_node(head.child), None
                    head.child = None
                    new_head.next = old_next
                    if old_next:
                        old_next.prev = new_head
                    head = new_head
                tail, head = head, head.next
            return tail

        process_node(head)
        return head
