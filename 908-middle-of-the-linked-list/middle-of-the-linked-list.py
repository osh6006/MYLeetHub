# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # 빠른 포인터는 두 배의 속도로 이동하고, 느린 포인터는 한 칸씩 이동합니다.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 느린 포인터는 중간 지점에 도달합니다.
        return slow



        
        