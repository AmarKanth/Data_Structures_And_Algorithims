class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def right_rotate(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotate(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    # if balance > 1 and get_balance(root_node.left_child) >= 0:
    #     return right_rotate(root_node)
    # if balance > 1 and get_balance(root_node.left_child) < 0:
    #     root_node.left_child = left_rotate(root_node.left_child)
    #     return right_rotate(root_node)
    # if balance < -1 and get_balance(root_node.right_child) <= 0:
    #     return left_rotate(root_node)
    # if balance < -1 and get_balance(root_node.right_child) > 0:
    #     root_node.right_child = right_rotate(root_node.right_child)
    #     return left_rotate(root_node)
    return root_node

def print_tree(root_node, level=0):
    if root_node:
        print_tree(root_node.left_child, level+1)
        print(" " * 4 * level + "->"+str(root_node.data))
        print_tree(root_node.right_child, level+1)

avl = AVLNode(30)
insert_node(avl, 20)
insert_node(avl, 40)
insert_node(avl, 60)
insert_node(avl, 55)
print_tree(avl)