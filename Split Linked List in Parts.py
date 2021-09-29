from typing import List, Optional
from stuff.ArrayToList import array_to_list, print_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        tmp_head = head
        n = 0
        while tmp_head:
            n += 1
            tmp_head = tmp_head.next
        
        res = []
        a, b = n // k, n % k
        for _ in range(k):
            if head:
                part = head
                for _ in range(a + (1 if b > 0 else 0)):
                    prev = head
                    head = head.next
                prev.next = None
                res.append(part)
                b -= 1
            else:
                break
        res += [None] * (k - len(res))
        return res


test = Solution()
for arr, k in zip([[1, 2, 3], [1,2,3,4,5,6,7,8,9,10]], [5, 3]):
    print(''.rjust(10, '='))
    res = test.splitListToParts(array_to_list(arr), k)
    for a in res:
        print_list(a)
