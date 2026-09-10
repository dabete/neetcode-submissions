# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # could potentially remove head so make a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # calculate the new length of the list
        length = 1
        length_pointer = dummy
        while length_pointer.next:
            length += 1
            length_pointer = length_pointer.next

        # calculate hop_value
        hop_value = length - n

        current = dummy
        for i in range(hop_value):
            current = current.next
        next_node = current.next

        current = dummy
        for i in range(hop_value - 1):
            current = current.next
        prev_node = current

        prev_node.next = next_node

        return dummy.next
        

        

        



        
            




        