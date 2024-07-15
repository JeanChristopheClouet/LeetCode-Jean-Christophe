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

        v = {}
        def dfs(n):
            if n in v:
                return v[n]
            c = Node(n.val)
            v[n]=c
            for nei in n.neighbors:
                c.neighbors.append(dfs(nei))
            return c

        return dfs(node) if node else None