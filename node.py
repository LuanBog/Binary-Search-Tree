# Left node is lesser than the root
# Right node is greater than the root

class Node:
    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None

    def get_node(self, value_to_find):
        node = self
        
        while node.value != value_to_find:
            node = node.right_node if node.value < value_to_find else node.left_node

        return node

    # def add_node(self, node):
    #     side_to_add = self.right_node if node.value < self.value else self.left_node
    #     side_to_add = node
