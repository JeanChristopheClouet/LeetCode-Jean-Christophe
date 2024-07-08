# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depths = []
        def traverse(node, depth):
            if node==None:
                depths.append(depth)
                return 
            else:
                traverse(node.left, depth+1)
                traverse(node.right, depth+1)
        
        traverse(root, 0)
        return max(depths)