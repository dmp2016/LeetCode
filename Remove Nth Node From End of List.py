from stuff.ArrayToList import array_to_list, print_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None, head)
        k = 0
        while head:
            head = head.next
            k += 1
        head = dummy
        for _ in range(k - n):
            head = head.next
        head.next = head.next.next
        return dummy.next


test = Solution()
print_list(test.removeNthFromEnd(head=array_to_list([1, 2, 3, 4, 5]), n=2))
print_list(test.removeNthFromEnd(head=array_to_list([1]), n=1))
print_list(test.removeNthFromEnd(head=array_to_list([1, 2]), n=1))
