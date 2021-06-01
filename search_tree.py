from node import Node

class Search_Tree:
    def __init__(self, list):
        self.list = list
        self.root_node = None
        
        self.grow_tree(list)

    def grow_tree(self, list):
        for value in list:
            new_node = Node(value)

            if not self.root_node:
                self.root_node = new_node
            else:
                node = self.root_node  
                
                while True:

                    if node.value < new_node.value:
                        if not node.right_node:
                            node.right_node = new_node
                            break
                        else:
                            node = node.right_node
                    else:
                        if not node.left_node:
                            node.left_node = new_node
                            break
                        else:
                            node = node.left_node

    def get_node(self, value_to_find):
        return self.root_node.get_node(value_to_find)

