class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_list = ListNode(-1)
        current = new_list
        while head:
            if head.val != val:
                new_list.next = ListNode(head.val)
                new_list = new_list.next
            head = head.next
        return current.next
