#!/usr/bin/env python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes_values = []

        def traverseHelper(tree_node):
            if not tree_node:
                return
            traverseHelper(tree_node.left)
            nodes_values.append(tree_node.val)
            traverseHelper(tree_node.right)
        traverseHelper(root)
        return nodes_values;
