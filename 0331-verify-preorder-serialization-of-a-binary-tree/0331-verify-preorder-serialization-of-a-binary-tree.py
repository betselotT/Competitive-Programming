class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        
        for node in preorder.split(','):
            degree -= 1 # Decrement the degree by 1 for each node
            
            if degree < 0: # If the degree is negative, return False
                return False
            
            if node != '#': # If the node is not a leaf node
                degree += 2 # Increment the degree by 2 for each non-leaf node
            
        return degree == 0