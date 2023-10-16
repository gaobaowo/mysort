# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head=None
dat=[1,2,4,3,5,9,1,2,4]
for x in dat:
    b=ListNode(x,head)
    head=b
a=head

left=3-1
right=7
while left>0:
    a=a.next
    left -=1
ll=a
s=ListNode(a.val)
while a.next !=None:
    a=a.next
    c=ListNode(a.val,s)
    s=c
      
ll.next=s

while head.next!=None:
    print(head.val)
    head=head.next