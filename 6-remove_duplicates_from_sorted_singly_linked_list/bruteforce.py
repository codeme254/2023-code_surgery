#!/usr/bin/env python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # only engage my algorithm if the list is actually defined
        current_node = head
        look_up = {}
        dummy_head_node = ListNode()
        append_position_pointer = dummy_head_node

        while current_node:
            if current_node.val in look_up.keys():
                current_node = current_node.next
            else:
                look_up[current_node.val] = True
                append_position_pointer.next = current_node
                current_node = current_node.next
                append_position_pointer = append_position_pointer.next
        print(look_up)
        return dummy_head_node.next
