from heapq import heappush, heappop
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        front = []
        res = ListNode(None)
        cur_res = res
        for ind in range(len(lists)):
            if lists[ind]:
                heappush(front, (lists[ind].val, ind))
                lists[ind] = lists[ind].next

        while len(front) > 0:
            val, cur = heappop(front)
            cur_res.next = ListNode(val, None)
            cur_res = cur_res.next
            if lists[cur]:
                heappush(front, (lists[cur].val, cur))
                lists[cur] = lists[cur].next
        return res.next


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


# print_list(array_to_list([1, 3, 8, -9, 10, 4]))
test = Solution()
print(print_list(test.mergeKLists(lists=[array_to_list([1, 4, 5]), array_to_list([1, 3, 4]), array_to_list([2, 6])])))
