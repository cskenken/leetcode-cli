# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.levelOrderHelper(root,0,[])
        
        
    def levelOrderHelper(self,node,level,ll=[]):
        if node==None:
            return []
        if len(ll)<level+1:
            ll.append([])
        ll[level].append(node.val)
        self.levelOrderHelper(node.left,level+1,ll)
        self.levelOrderHelper(node.right,level+1,ll)
        return ll
        