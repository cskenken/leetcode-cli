# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        每次只需要求左右子树高度的最大值，加上1，就是树的高度
        """
        if root==None:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return max(left_depth,right_depth) + 1