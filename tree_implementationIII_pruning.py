# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self,child_node):
    print("Removing "+ child_node.value + "from " + self.value)
    
    new_children = [child for child in self.children if child != child_node]
    self.children = new_children
    # for i in self.children:
    #   if i != child_node:
    #     new_children.append(i)
    # self.children = new_children


root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

'''
Adding A wee sappling
Adding Root Rot!
Removing Root Rot!from I am Root

'''