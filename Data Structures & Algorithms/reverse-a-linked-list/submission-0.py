# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we are given 'head' 
        # what we need to do:
        # reverse the list and return the new beginning of the list - i imagine by new beginning they mean the new head of the list
        

        # figure out the tail of the list - which will become the new head 

        if (head == None):
            return head

        list1 = []
        while head.next:
            list1.append(head.val)
            head = head.next

        list1.append(head.val)

        list1.reverse()

        print(list1)

        head = ListNode(list1[0], None)
        current = head
        for i in range(1, len(list1)):
            current.next = ListNode(list1[i], None)
            current = current.next

        return head

        