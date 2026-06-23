# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        current = new_list
        

        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            if temp1.val > temp2.val:
                current.next = temp2
                temp2 = temp2.next
            
            # elif temp1.val < temp2.val:
            #     new_list.next = temp1
            #     temp1 = temp1.next
            else:
                current.next = temp1
                temp1 = temp1.next
            current = current.next

        current.next  = temp1 if temp1 else temp2

        print(new_list)
        return new_list.next
        