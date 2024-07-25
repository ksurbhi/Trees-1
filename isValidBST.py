# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##################  Method 1 #################
class Solution:
    """
    Time Complexity: O(n) - The algorithm visits each node once.
    Space Complexity: O(h) - The space required for the recursion stack, 
    where h is the height of the tree. In the worst case, this can be O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If the root is None, the tree is considered valid.
        if root is None:
            return True
        
        # Initialize variables to track the previous node in the in-order traversal
        # and a flag to determine if the tree is valid.
        self.previous = None
        self.isValid = True
        
        # Perform in-order traversal to check the validity of the BST.
        self.inOrder(root)
        
        # Return the result.
        return self.isValid
    
    def inOrder(self, root: Optional[TreeNode]):
        # Base case: if the current node is None, return.
        if root is None:
            return
        
        # Traverse the left subtree.
        self.inOrder(root.left)
        
        # If the previous node is not None and its value is greater than or equal to the
        # current node's value, the tree is not a valid BST.
        if self.previous is not None and self.previous.val >= root.val:
            self.isValid = False
            return
        
        # Update the previous node to the current node.
        self.previous = root
        
        # Traverse the right subtree.
        self.inOrder(root.right)


############### Method 2 ##################

class Solution:
   """
    Time Complexity: O(n) - The algorithm visits each node once.
    Space Complexity: O(h) - The space required for the recursion stack, 
    where h is the height of the tree. In the worst case, this can be O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it's considered a valid BST.
        if root is None:
            return True
        
        # Initialize a flag to determine if the tree is valid.
        self.isValid = True
        
        # Perform depth-first search (DFS) to check the validity of the BST.
        self.dfs(root, None, None)
        
        # Return the result.
        return self.isValid

    def dfs(self, root, Min, Max):
        # Base case: if the current node is None, return.
        if root is None:
            return
        
        # If the current node's value is not within the valid range, set the flag to False.
        if (Min is not None and root.val <= Min) or (Max is not None and root.val >= Max):
            self.isValid = False
            return
        
        # Recursively check the left subtree with updated maximum value.
        self.dfs(root.left, Min, root.val)
        
        # Recursively check the right subtree with updated minimum value.
        self.dfs(root.right, root.val, Max)
     
