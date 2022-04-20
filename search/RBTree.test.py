from RBTree import RBNode, RBTree

n = [20,15,14,12,13,1]
n_node = [ RBNode(x) for x in n ]

rbtree = RBTree()

for node in n_node :
    rbtree.insert(node)
    rbtree.print_tree()

print(rbtree.root.parent.value)