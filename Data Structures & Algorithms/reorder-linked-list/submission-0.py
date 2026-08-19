# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # given the head of a singly linked list 'head'

        # re order in 0, n-1, 1, n-2, 2, n-3, 3, ... etc

        # have to actually reorder nodes, cannot modify the value of the nodes themselves

        # to start off, head = 0 will stay the same position

        # topics mention two pointers, idk why i didn't think of that

        # instead of left and right could use head and tail? but it is singly linked so how would i do that

        # first i want to try using a brute force approach

        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        nodes_rearranged = []

    
        for i in range(len(nodes) // 2):
            nodes_rearranged.append(nodes[i])
            nodes_rearranged.append(nodes[len(nodes) - 1 - i])

        if len(nodes) % 2 != 0:
            nodes_rearranged.append(nodes[len(nodes) // 2])

        nodes_rearranged[-1].next = None

        # now construct the linked list from the array

        for i in range(1, len(nodes_rearranged)):
            head.next = nodes_rearranged[i]
            head = head.next


        # i forgot that i have to set the last nodes next pointer to None otherwise it creates a cycle and therefore infinite loop
    


        

        
        
                


            

        


        