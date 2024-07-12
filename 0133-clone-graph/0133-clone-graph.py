"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        traversed = {}

        def dfs(root):
            if root in traversed:
                return traversed[root]
            else:
                copy = Node(root.val)
                traversed[root]=copy
                for nei in root.neighbors:
                    copy.neighbors.append(dfs(nei))
                return copy
        
        return dfs(node) if node else None