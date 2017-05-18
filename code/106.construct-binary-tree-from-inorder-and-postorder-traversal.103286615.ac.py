# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
    
        dict_inorder={}
        i=0
        for x in inorder:
            dict_inorder[x]=i
            i+=1
        root=self.buildTreeHelper(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,dict_inorder)
        return root
        
    def buildTreeHelper(self,inorder,s0,e0,postorder,s1,e1,dict_inorder):
        if s0>e0 or s1>e1:
            return None
        
        mid=dict_inorder[postorder[e1]]
        num=mid-s0
        
        node=TreeNode(postorder[e1])
        
        node.left=self.buildTreeHelper(inorder,s0,mid-1,postorder,s1,s1+num-1,dict_inorder)
        node.right=self.buildTreeHelper(inorder,mid+1,e0,postorder,s1+num,e1-1,dict_inorder)
        
        return node
        
        
        
            
    