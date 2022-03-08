from typing import List


# Definition for singly-linked list.
class ListNode:
    # def __init__(self, data: List):
    #     head = self
    #     for val in data:
    #         head.val = val
    #         head.next = 

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = slow.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


test = Solution()
node = ListNode(3)
a = dict()
a[node] = 0
b = set()
b.add(node)
