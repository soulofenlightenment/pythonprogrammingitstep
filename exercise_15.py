class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

                    # 10    11
    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)
        
######## ჩემი დავალება  ############

    #leaf node
    def _leaf_node(self,node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.key)
        else:
            self._leaf_node(node.left)
            self._leaf_node(node.right)

    def leaf_node(self):
        self._leaf_node(self.root)
tree = BST()
