# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        def right(root):
            if root is None:
                return []
            queue=deque()
            queue.append(root)
            while queue:
                n=len(queue)
                right_node=None
                for i in range(n):
                    node=queue.popleft()
                    right_node=node
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                result.append(right_node.val)
        right(root)
        return result
                    
            
        