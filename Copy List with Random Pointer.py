from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur:
            new_node = Node(cur.val)
            cur.next, new_node.next = new_node, cur.next
            cur = new_node.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur = head
        new_head = head.next
        cur_new = new_head

        cur.next = cur_new.next
        cur = cur.next
        while cur:
            cur_new.next = cur.next
            cur_new = cur.next
            cur.next = cur_new.next
            cur = cur.next
        cur_new.next = None
        return new_head
