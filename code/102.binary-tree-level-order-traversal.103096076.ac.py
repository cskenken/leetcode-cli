# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ll=[]
        if root==None:
            return ll
        q=deque([])
        q.append(root)
        
        while len(q):
            size=len(q)
            level_list=[]
            for i in xrange(size):
                node=q.popleft()
                level_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ll.append(level_list)
        return ll
        
        