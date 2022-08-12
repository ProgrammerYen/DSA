class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
        
def create_tree(data):
    """Creates a tree of values from given data."""
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = create_tree(data[0])
        node.right = create_tree(data[-1])
        
    elif data is None:
        node = None
        
    else:
        node = TreeNode(data)
        
    return node
    
     
tree_tuple = create_tree(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))  
print(tree_tuple)