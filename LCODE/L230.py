# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        auxiliary = []
        def inorder(root, auxiliary):
            if root == None:
                return auxiliary
            inorder(root.left, auxiliary)
            auxiliary.append(root.val)
            inorder(root.right, auxiliary)
            
        inorder(root, auxiliary)
        result = auxiliary[k - 1]
        return result