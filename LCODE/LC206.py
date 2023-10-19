# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=None
        b=ListNode()
        if head==None:
            return None
        while head!=None:
            b=ListNode(head.val,a)
            a=b
            head=head.next
        return b