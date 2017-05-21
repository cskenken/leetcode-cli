# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        else:
            return self.isSymmetricHelper(root.left,root.right)
        
        
            
    def isSymmetricHelper(self,node1,node2):
        if node1==None:
            return node2==None
        if node2==None:
            return node1==None
        if node1.val==node2.val:
            return self.isSymmetricHelper(node1.left,node2.right) and self.isSymmetricHelper(node1.right,node2.left)
        return False
        
            