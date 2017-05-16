# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        求最小深度和求最大深度相似，但是注意斜树的情况。
        当左侧子树深度为0时，返回右侧子树的深度+1
        当右侧子树深度为0时，返回左侧子树的深度+1
        """
        if root==None:
            return 0
        left_depth=self.minDepth(root.left)
        right_depth=self.minDepth(root.right)
        if left_depth==0:
            return right_depth+1
        if right_depth==0:
            return left_depth+1
        return min(left_depth,right_depth)+1
        