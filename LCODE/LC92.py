# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 建立链表
head=None
dat=[9,8,7,6,5,4,3,2,1]
for x in dat:
    b=ListNode(x,head)
    head=b
a=head
# 找到链表中的LEFT位置
left=3-1
right=7-3-1
while left>0:
    a=a.next
    left -=1
#ll指向Left
ll=a
pa=a
a=a.next
print("-----------------")

s=ListNode(a.val)
ss=s
while right>0:
    a=a.next
    c=ListNode(a.val,s)
    s=c
    right -= 1
      
pa.next=s
ss.next=a.next

while head.next!=None:
    print(head.val)
    head=head.next
print(head.val)
print(f'ss={ss.val}')