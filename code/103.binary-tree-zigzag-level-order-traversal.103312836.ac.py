# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ls=self.zigzagLevelOrderHelper(root,0,[])
        i=1
        while i<len(ls):
            ls[i].reverse()
            i+=2
        return ls
        
        
    def zigzagLevelOrderHelper(self,node,level,ll=[]):
        if node==None:
            return []
        if len(ll)<level+1:
            ll.append([])
        ll[level].append(node.val)
        self.zigzagLevelOrderHelper(node.left,level+1,ll)
        self.zigzagLevelOrderHelper(node.right,level+1,ll)
        return ll