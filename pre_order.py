def pre_order(tree):
    visit_order = list()
    
    def traverse(node):
        if node:
            #visit the node
            visit_order.append(node.get_value())


            #traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree

            traverse(node.get_right_child())

    traverse(tree.get_root())
    return visit_order


def in_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # visit node
            visit_order.append(node.get_value())
            
            # traverse right sub-tree
            traverse(node.get_right_child())
    
    traverse(tree.get_root())
    
    return visit_order

# check solution: should get: ['dates', 'banana', 'apple', 'cherry']


# solution
def post_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # traverse right subtree
            traverse(node.get_right_child())
            
            # visit node
            visit_order.append(node.get_value())
    
    traverse(tree.get_root())
    
    return visit_order

# check solution: should get: ['dates', 'banana', 'cherry', 'apple']