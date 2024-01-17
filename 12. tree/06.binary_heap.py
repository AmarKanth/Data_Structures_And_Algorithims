"""
                        TimeComplexity      SpaceComplexity
peak_of_heap            O(1)                O(1)
size_of_heap            O(1)                O(1)
level_order_traversal   O(n)                O(1)
insert_node             O(logN)             O(logN)
extract_node            O(logN)             O(logN)
delete_bh               O(1)                O(1)
"""
class Heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

def peak_of_heap(root_node):
    if not root_node:
        return
    return root_node.custom_list[1]

def size_of_heap(root_node):
    if not root_node:
        return
    return root_node.heap_size

def level_order_traversal(root_node):
    if not root_node:
        return
    for idx in range(1, root_node.heap_size+1):
        print(root_node.custom_list[idx])

def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index/2)
    if index <= 1:
        return
    
    # Performed element swapping for sorting.
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
            heapify_tree_insert(root_node, parent_index, heap_type)
    if heap_type == "Max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
            heapify_tree_insert(root_node, parent_index, heap_type)

def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "Binary Heap is full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    # Heapifying will be performed from last node to rootnode
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value is successfully inserted"

def heapify_tree_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_index:
        return 
    # If current node has only leftchild and leftchild is the last child
    elif root_node.heap_size == left_index:
        if heap_type == "Min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    # If current node has right and left child
    else:
        if heap_type == "Min":
            # Find Min value between left and right childs
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[swap_child]
            root_node.custom_list[swap_child] = temp
        else:
            # Find Max value between left and right childs
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[swap_child]
            root_node.custom_list[swap_child] = temp
    heapify_tree_extract(root_node, swap_child, heap_type)

def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        # Binary Heap allowed to extract rootNode
        extracted_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        # Heapifying will be performed from rootNode
        heapify_tree_extract(root_node, 1, heap_type)
        return extracted_node
    
def delete_bh(root_node):
    root_node.custom_list = None

new_binary_heap = Heap(5)
insert_node(new_binary_heap, 4, "Max")
insert_node(new_binary_heap, 5, "Max")
insert_node(new_binary_heap, 2, "Max")
insert_node(new_binary_heap, 1, "Max")
level_order_traversal(new_binary_heap)