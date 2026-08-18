# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if i remember correctly a cycle you get two pointers and make one twice the speed of the other, if they meet then you have a cycle

        # given 'head'

        hashset = set()

        while head:
            if head in hashset:
                return True
            else:
                hashset.add(head)
                head = head.next

        return False
        