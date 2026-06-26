# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        # print(slow.val,"second half", second_half.val)

        prev = None
        curr =  second_half
        while curr is not None:
            NEXT = curr.next
            curr.next = prev
            prev = curr
            curr = NEXT
        
        # print("first half", head.val)
        # print("second half",prev.val) 

        first, second = head, prev
        # print("temp1", temp1.val, "temp2", temp2.val)
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
            

