class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value =value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value 

    def set_value(self,data):
        self.value = data
    
    def get_left_child(self):
        return self.left 
    
    def set_left_child(self,node):
        self.left = node 

    def get_right_child(self):
        return self.right 
    
    def set_right_child(self,node):
        self.right = node

    def has_left_child(self):
        if self.left:
            return True 
        else:
            return False 

    def has_right_child(self):
        if self.right:
            return True 
        else:
            return False 

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")


class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def get_root(self):
        return self.root 