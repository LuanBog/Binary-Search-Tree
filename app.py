#! /usr/bin/env python

from node import Node

root_node = Node(20)
sixteen = Node(16)
twentyfive = Node(25)
six = Node(6)
seventeen = Node(17)
twentyone = Node(21)
twentynine = Node(29)
zero = Node(0)
seven = Node(7)
twentyeight = Node(28)
fiftyone = Node(51)
fourtysix = Node(46)

root_node.left_node = sixteen
root_node.right_node = twentyfive

sixteen.left_node = six
sixteen.right_node = seventeen

twentyfive.left = twentyone
twentyfive.right_node = twentynine

six.left_node = zero
six.right_node = seven

twentynine.left_node = twentyeight
twentynine.right_node = fiftyone

fiftyone.left_node = fourtysix

print(root_node.get_node(46).value)

# Todo: Create a more organized way when creating a tree
