class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        
        def traverse(root):
            if not root:
                return True
                        
            if root.val is not val:
                return False
            
            return (traverse(root.left) and traverse(root.right))
        
        return traverse(root
