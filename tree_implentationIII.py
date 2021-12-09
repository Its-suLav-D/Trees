class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = list()

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)


root = TreeNode("I am a Root")
child = TreeNode("A wee sappling")

root.add_child(child)