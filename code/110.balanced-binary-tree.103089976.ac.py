# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    采用递归方式，每次获得左右子树的深度，判断左右子树是否满足平衡条件
    使用辅助的函数获得树的深度
    此种方法中有重复递归
    """
    """
    def isBalanced(self, root):
        if root==None:
            return True
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        diff=left_depth-right_depth
        if abs(diff)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        
    def maxDepth(self,root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
    """
    
    """
    可以将获得深度和判断平衡放在一起，因为都是类似后序遍历,在获得子对象的信息之后再做相应操作
    """
    def isBalanced(self,root):
        
        return self.solve(root)[1]
    
    def solve(self,root):
        if root==None:
            return [0,True]
        tmp1_left=self.solve(root.left)
        tmp2_right=self.solve(root.right)
        depth=max(tmp1_left[0],tmp2_right[0])+1
        
        if abs(tmp1_left[0]-tmp2_right[0])>1:
            return [depth,False]
        else:
            return [depth,tmp1_left[1] and tmp2_right[1]]
            
            
        
        
        
        
    
    