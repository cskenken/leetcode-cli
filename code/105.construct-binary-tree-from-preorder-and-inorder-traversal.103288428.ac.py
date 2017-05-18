# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict_inorder={}
        i=0
        for x in inorder:
            dict_inorder[x]=i
            i+=1
        root=self.buildTreeHelper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,dict_inorder)
        return root
        
    
    def buildTreeHelper(self,preorder,s0,e0,inorder,s1,e1,dict_inorder):
        if s0>e0 or s1>e1:
            return None
        
        mid=dict_inorder[preorder[s0]]
        num=mid-s1
        
        node=TreeNode(preorder[s0])
        
        node.left=self.buildTreeHelper(preorder,s0+1,s0+num,inorder,s1,mid-1,dict_inorder)
        node.right=self.buildTreeHelper(preorder,s0+num+1,e0,inorder,mid+1,e1,dict_inorder)
        return node
        
        
        
        