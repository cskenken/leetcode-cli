# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ls=self.levelOrderBottomHelper(root,0,[])
        ls.reverse()
        return ls
    
    
    def levelOrderBottomHelper(self,node,level,ll=[]):
        if node==None:
            return []
        if len(ll)<level+1:
            ll.append([])
        ll[level].append(node.val)
        self.levelOrderBottomHelper(node.left,level+1,ll)
        self.levelOrderBottomHelper(node.right,level+1,ll)
        return ll
        
        
        