from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odds = ListNode()
        odds_head = dummy_odds
        dummy_evens = ListNode()
        evens_head = dummy_evens
        ind = 1
        while head:
            if ind & 1:
                odds_head.next = head
                odds_head = head
            else:
                evens_head.next = head
                evens_head = head
            head = head.next
            ind += 1
        evens_head.next = None
        odds_head.next = dummy_evens.next
        return dummy_odds.next


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


test = Solution()
print_list(test.oddEvenList(array_to_list([1, 2, 3, 4, 5])))
print_list(test.oddEvenList(array_to_list([2, 1, 3, 5, 6, 4, 7])))
