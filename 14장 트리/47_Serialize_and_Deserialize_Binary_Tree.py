# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            length = len(queue)
            node = queue.pop()
            if node:
                result.append(node.val)
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                result.append(None)
                    
        return ' '.join(list(map(str, result)))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None
        
        data_list = collections.deque(list(map(str, data.split())))
        root = TreeNode(data_list.popleft())
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            left = data_list.popleft()
            right = data_list.popleft()
            
            if left != 'None':
                node.left = TreeNode(left)
                queue.append(node.left)
            if right != 'None':
                node.right = TreeNode(right)
                queue.append(node.right)
                
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
