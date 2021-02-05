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
        while head is not None:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False


test = Solution()
node = ListNode(3)
a = dict()
a[node] = 0
b = set()
b.add(node)
