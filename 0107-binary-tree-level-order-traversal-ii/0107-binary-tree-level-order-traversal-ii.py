# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        def level(root):
            if root is None:
                return []
            
            
            queue=deque([root])
            
            while queue:
                current=[]
                n=len(queue)
                for i in range(n):
                    node=queue.popleft()
                    current.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                result.append(current)
        level(root)
        return result[::-1]
        