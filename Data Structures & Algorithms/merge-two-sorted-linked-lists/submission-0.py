# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # heads - 'list1' and 'list2'

        # we need to merge the two in a way that is sorted
        # use technique similar to merge sort

        # edge checks

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1 == None and list2 == None:
            return None

        # get the head first
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next

        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        return head
            

        

        