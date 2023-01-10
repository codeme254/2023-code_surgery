#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      list_one_pointer = list1
      list_two_pointer = list2
      dummy_head_node = ListNode()
      current_append_position = dummy_head_node

      while list_one_pointer and list_two_pointer:
          if list_two_pointer.val < list_one_pointer.val:
              current_append_position.next = list_two_pointer
              current_append_position = current_append_position.next
              list_two_pointer = list_two_pointer.next
          else:
              current_append_position.next = list_one_pointer
              current_append_position = current_append_position.next
              list_one_pointer = list_one_pointer.next
          print("working")

      while list_one_pointer:
          current_append_position.next = list_one_pointer
          current_append_position = current_append_position.next
          list_one_pointer = list_one_pointer.next

      while list_two_pointer:
          current_append_position.next = list_two_pointer
          current_append_position = current_append_position.next
          list_two_pointer = list_two_pointer.next

      return dummy_head_node.next
