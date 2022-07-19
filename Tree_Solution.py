class BST:
    def __init__(self,data):
        node = self.node(data)
        self.root = node

    class node:
        def __init__(self,data):
            self.left = None
            self.right = None

            self.data = data

    def insert(self, data):
        self._insert(data, self.root)

    def _insert(self,data,node):
        
        if data < node.data:
            if node.left is None:
                # base case for the left side
                node.left = self.node(data)
            else:
                # use recursion to keep checking
                self._insert(data, node.left)

        
        elif data >= node.data:
            if node.right is None:
                # second base case for the right side
                node.right = self.node(data)
            else:
                # use recursion to keep checking
                self._insert(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)
    
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


bst = BST(7)

bst.insert(9)
bst.insert(8)
bst.insert(12)
bst.insert(4)
bst.insert(6)
bst.insert(1)

for number in bst:
    print(number)

# 1
# 4
# 6
# 7
# 8
# 9
# 12

print('--------------')
# apply a temporary change using numbers from the whole tree
for number in bst:
    number += 1
    print(number)

# 2
# 5
# 7
# 8
# 9
# 10
# 13