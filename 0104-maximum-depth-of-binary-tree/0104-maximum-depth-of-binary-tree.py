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

        def traverse(Node, depth):
            if type(Node) != TreeNode:
                depths.append(0)
                return 0
            if Node.left==None and Node.right==None:
                depths.append(depth)
                return depth
            elif Node.right!=None and Node.right!=None:
                traverse(Node.left, depth+1)
                traverse(Node.right, depth+1)
                return
            elif Node.left!=None:
                depth1 = depth+1
                traverse(Node.left, depth1)
                return 
            elif Node.right!=None:
                depth2 = depth+1
                traverse(Node.right, depth2)
                return
            else:
                return
            
        traverse(root, 1)
        return max(depths)
            

        